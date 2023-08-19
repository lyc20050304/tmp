const gridSize = 9;

const sudokuGrid = document.getElementById("sudoku-grid");
const solveButton = document.getElementById("solve-btn");

function isValidMove(board, row, col, num) {
  for (let i = 0; i < gridSize; i++) {
    if (board[row][i] === num || board[i][col] === num) return false;
  }

  const startRow = Math.floor(row / 3) * 3;
  const startCol = Math.floor(col / 3) * 3;
  for (let i = startRow; i < startRow + 3; i++) {
    for (let j = startCol; j < startCol + 3; j++) {
      if (board[i][j] === num) return false;
    }
  }

  return true;
}
function solveSudokuHelper(board) {
  for (let row = 0; row < gridSize; row++) {
    for (let col = 0; col < gridSize; col++) {
      if (board[row][col] === 0) {
        for (let num = 1; num <= 9; num++) {
          if (isValidMove(board, row, col, num)) {
            board[row][col] = num;
            if (solveSudokuHelper(board)) return true;

            board[row][col] = 0;
          }
        }
        return false;
      }
    }
  }
  return true;
}
function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}
async function solveSudoku() {
  const sudokuArray = [];
  for (let row = 0; row < gridSize; row++) {
    sudokuArray[row] = [];
    for (let col = 0; col < gridSize; col++) {
      const cellId = `cell-${row}-${col}`;
      const cellValue = document.getElementById(cellId).value;
      sudokuArray[row][col] = cellValue !== "" ? parseInt(cellValue) : 0;
    }
  }

  for (let row = 0; row < gridSize; row++) {
    for (let col = 0; col < gridSize; col++) {
      const cellId = `cell-${row}-${col}`;
      const cell = document.getElementById(cellId);
      if (sudokuArray[row][col] !== 0) {
        cell.classList.add("user-input");
      }
    }
  }

  if (solveSudokuHelper(sudokuArray)) {
    for (let row = 0; row < gridSize; row++) {
      for (let col = 0; col < gridSize; col++) {
        const cellId = `cell-${row}-${col}`;
        const cell = document.getElementById(cellId);
        if (!cell.classList.contains("user-input")) {
          cell.classList.add("solved");
          cell.value = sudokuArray[row][col];
          await sleep(20);
        }
      }
    }
  } else {
    alert("No solution exists for the given Sudoku puzzle.");
  }
}
document.addEventListener("DOMContentLoaded", () => {
  solveButton.addEventListener("click", solveSudoku);

  for (let row = 0; row < gridSize; row++) {
    const newRow = document.createElement("tr");
    for (let col = 0; col < gridSize; col++) {
      const input = document.createElement("input");
      const cell = document.createElement("td");
      input.className = "cell";
      input.id = `cell-${row}-${col}`;
      input.type = "number";
      cell.appendChild(input);
      newRow.appendChild(cell);
    }
    sudokuGrid.appendChild(newRow);
  }
});
