import streamlit as st
import stripe
import os
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker
import bcrypt

# -----------------------------------------------------------------------------
# 1. SETUP STRIPE & DATABASE
# -----------------------------------------------------------------------------
# Securely retrieve the Stripe Secret Key from Streamlit Secrets or Environment Variables
stripe.api_key = st.secrets.get("STRIPE_SECRET_KEY", os.getenv("STRIPE_SECRET_KEY"))

engine = create_engine('sqlite:///streamlit_eshop.db')
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    image_url = Column(String)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
db_session = Session()

# Seed initial sample products if database is empty
if db_session.query(Product).count() == 0:
    p1 = Product(name="Python T-Shirt", price=19.99, image_url="https://images.unsplash.com/photo-1521572267360-ee0c2909d518?w=300")
    p2 = Product(name="Developer Mug", price=9.99, image_url="https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?w=300" )
    db_session.add_all([p1, p2])
    db_session.commit()

# -----------------------------------------------------------------------------
# 2. STATE MANAGEMENT (Session / Cart / Login Status)
# -----------------------------------------------------------------------------
if 'cart' not in st.session_state:
    st.session_state.cart = {}  # Format: {product_id: quantity}

if 'user' not in st.session_state:
    st.session_state.user = None

# -----------------------------------------------------------------------------
# 3. SIDEBAR: AUTHENTICATION & USER INFO
# -----------------------------------------------------------------------------
st.sidebar.title("👤 Account")

if st.session_state.user is None:
    auth_mode = st.sidebar.radio("Choose Action:", ["Login", "Register"])
    email = st.sidebar.text_input("Email")
    password = st.sidebar.text_input("Password", type="password")

    if auth_mode == "Register" and st.sidebar.button("Create Account"):
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        new_user = User(email=email, password=hashed)
        try:
            db_session.add(new_user)
            db_session.commit()
            st.session_state.user = email
            st.sidebar.success("Registration successful!")
            st.rerun()
        except Exception:
            st.sidebar.error("Email already exists!")

    elif auth_mode == "Login" and st.sidebar.button("Log In"):
        user = db_session.query(User).filter_by(email=email).first()
        if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            st.session_state.user = user.email
            st.sidebar.success("Logged in successfully!")
            st.rerun()
        else:
            st.sidebar.error("Invalid credentials!")
else:
    st.sidebar.write(f"Welcome, **{st.session_state.user}**!")
    if st.sidebar.button("Log Out"):
        st.session_state.user = None
        st.rerun()

# -----------------------------------------------------------------------------
# 4. MAIN PAGE: PRODUCTS DISPLAY
# -----------------------------------------------------------------------------
st.title("🛒 Python E-Shop")

products = db_session.query(Product).all()
cols = st.columns(len(products))

for idx, product in enumerate(products):
    with cols[idx]:
        st.image(product.image_url, width=150)
        st.subheader(product.name)
        st.write(f"**Price:** €{product.price}")
        if st.button("➕ Add to Cart", key=f"btn_{product.id}"):
            st.session_state.cart[product.id] = st.session_state.cart.get(product.id, 0) + 1
            st.success("Added to cart!")

st.divider()

# -----------------------------------------------------------------------------
# 5. CART & STRIPE CHECKOUT
# -----------------------------------------------------------------------------
st.header("🛍️ Shopping Cart")

if st.session_state.cart:
    total_amount = 0
    line_items = []

    for p_id, qty in st.session_state.cart.items():
        p = db_session.query(Product).get(p_id)
        subtotal = p.price * qty
        total_amount += subtotal
        st.write(f"• **{p.name}** x {qty} — €{subtotal:.2f}")

        # Construct payload for Stripe API
        line_items.append({
            'price_data': {
                'currency': 'eur',
                'product_data': {'name': p.name},
                'unit_amount': int(p.price * 100),  # Stripe expects price in cents
            },
            'quantity': qty,
        })

    st.write(f"### **Total: €{total_amount:.2f}**")

    if st.button("🗑️ Clear Cart"):
        st.session_state.cart = {}
        st.rerun()

    # CHECKOUT WITH STRIPE
    if st.session_state.user:
        if st.button("💳 Pay with Stripe"):
            try:
                checkout_session = stripe.checkout.Session.create(
                    payment_method_types=['card'],
                    line_items=line_items,
                    mode='payment',
                    success_url="https://streamlit.io",  # Target redirect URL upon success
                    cancel_url="https://streamlit.io",   # Target redirect URL upon cancellation
                )
                st.link_button("👉 Click here to complete payment on Stripe", checkout_session.url)
            except Exception as e:
                st.error(f"Stripe Error: {e}")
    else:
        st.warning("Please log in via the sidebar to proceed to checkout.")
else:
    st.info("Your cart is empty.")