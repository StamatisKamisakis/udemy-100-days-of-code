import streamlit as st
import requests

st.set_page_config(page_title="Book Search API", page_icon="📚")

st.title("📚 Book Finder (REST API)")
st.caption("Day 96 Project - 100 Days of Code (Python)")

# User input field
query = st.text_input("Enter a book title or topic:", placeholder="e.g. Harry Potter, Python")

if st.button("Search") or query:
    if query.strip():
        url = f"https://openlibrary.org/search.json?q={query}"
        
        with st.spinner("Fetching data from Open Library API..."):
            try:
                # HTTP GET Request
                response = requests.get(url)
                response.raise_for_status()
                data = response.json()
                
                docs = data.get("docs", [])[:5]
                
                if docs:
                    st.subheader(f"Top results for '{query}':")
                    for book in docs:
                        title = book.get("title", "No title available")
                        author = book.get("author_name", ["Unknown Author"])[0]
                        year = book.get("first_publish_year", "N/A")
                        
                        # Display results inside clean UI cards
                        with st.container():
                            st.markdown(f"### 📖 {title}")
                            st.write(f"**Author:** {author}")
                            st.write(f"**First Published:** {year}")
                            st.divider()
                else:
                    st.warning("No books found.")
            except requests.exceptions.RequestException as e:
                st.error(f"API Error: {e}")
    else:
        st.info("Please enter a search term.")
