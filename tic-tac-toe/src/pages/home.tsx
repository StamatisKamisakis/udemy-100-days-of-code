import { useState } from "react";

type Player = "X" | "O" | null;

const WIN_CONDITIONS = [
  [0, 1, 2], [3, 4, 5], [6, 7, 8],
  [0, 3, 6], [1, 4, 7], [2, 5, 8],
  [0, 4, 8], [2, 4, 6]
];

function checkWinner(squares: Player[]): { player: Player | "Draw"; line: number[] } | null {
  for (const [a, b, c] of WIN_CONDITIONS) {
    if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
      return { player: squares[a], line: [a, b, c] };
    }
  }
  if (!squares.includes(null)) return { player: "Draw", line: [] };
  return null;
}

export default function Home() {
  const [board, setBoard] = useState<Player[]>(Array(9).fill(null));
  const [xIsNext, setXIsNext] = useState(true);
  const [scores, setScores] = useState({ X: 0, O: 0, draws: 0 });
  const [result, setResult] = useState<{ player: Player | "Draw"; line: number[] } | null>(null);

  const currentPlayer = xIsNext ? "X" : "O";

  const handleClick = (i: number) => {
    if (board[i] || result) return;
    const next = [...board];
    next[i] = currentPlayer;
    setBoard(next);
    const res = checkWinner(next);
    if (res) {
      setResult(res);
      if (res.player === "X") setScores(s => ({ ...s, X: s.X + 1 }));
      else if (res.player === "O") setScores(s => ({ ...s, O: s.O + 1 }));
      else setScores(s => ({ ...s, draws: s.draws + 1 }));
    } else {
      setXIsNext(!xIsNext);
    }
  };

  const reset = () => {
    setBoard(Array(9).fill(null));
    setXIsNext(true);
    setResult(null);
  };

  const getStatus = () => {
    if (!result) return `Turn: Player ${currentPlayer}`;
    if (result.player === "Draw") return "🤝 It's a Draw!";
    return `🎉 Player ${result.player} Wins!`;
  };

  return (
    <div style={{
      minHeight: "100vh",
      display: "flex",
      flexDirection: "column",
      alignItems: "center",
      justifyContent: "center",
      background: "#1a1a2e",
      fontFamily: "Arial, sans-serif",
    }}>
      <h1 style={{ fontSize: 32, fontWeight: "bold", marginBottom: 8, color: "#e0e0e0" }}>
        Tic Tac Toe
      </h1>

      {/* Scores */}
      <div style={{ display: "flex", gap: 32, marginBottom: 20 }}>
        <div style={{ textAlign: "center" }}>
          <div style={{ fontSize: 22, fontWeight: "bold", color: "#fc8181" }}>{scores.X}</div>
          <div style={{ fontSize: 13, color: "#aaa" }}>Player X</div>
        </div>
        <div style={{ textAlign: "center" }}>
          <div style={{ fontSize: 22, fontWeight: "bold", color: "#aaa" }}>{scores.draws}</div>
          <div style={{ fontSize: 13, color: "#aaa" }}>Draws</div>
        </div>
        <div style={{ textAlign: "center" }}>
          <div style={{ fontSize: 22, fontWeight: "bold", color: "#63b3ed" }}>{scores.O}</div>
          <div style={{ fontSize: 13, color: "#aaa" }}>Player O</div>
        </div>
      </div>

      {/* Status */}
      <div style={{ fontSize: 20, fontWeight: "600", marginBottom: 16, color: "#e0e0e0", minHeight: 30 }}>
        {getStatus()}
      </div>

      {/* Board */}
      <div style={{
        display: "grid",
        gridTemplateColumns: "repeat(3, 100px)",
        gridTemplateRows: "repeat(3, 100px)",
        gap: "3px",
        background: "#444",
        border: "3px solid #444",
      }}>
        {board.map((cell, i) => {
          const isWin = result?.line.includes(i);
          return (
            <button
              key={i}
              onClick={() => handleClick(i)}
              data-testid={`cell-${i}`}
              style={{
                width: 100,
                height: 100,
                background: isWin
                  ? (result?.player === "X" ? "#742a2a" : "#1a365d")
                  : "#16213e",
                border: "none",
                fontSize: 48,
                fontWeight: "bold",
                cursor: cell || result ? "default" : "pointer",
                color: cell === "X" ? "#fc8181" : "#63b3ed",
                transition: "background 0.2s",
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
              }}
            >
              {cell}
            </button>
          );
        })}
      </div>

      {/* New Game Button */}
      <button
        onClick={reset}
        data-testid="button-new-game"
        style={{
          marginTop: 24,
          padding: "10px 32px",
          fontSize: 16,
          fontWeight: "bold",
          background: "#e0e0e0",
          color: "#1a1a2e",
          border: "none",
          borderRadius: 8,
          cursor: "pointer",
        }}
      >
        New Game
      </button>
    </div>
  );
}
