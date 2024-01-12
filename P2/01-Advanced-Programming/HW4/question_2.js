
function CheckSudoku(board) {
    let n = board.length;
    let sqrtn = Math.sqrt(n);

    function validate(list) {
        let checked = new Map();
        let repeat = new Map();
        for (let digit of list) {
            if (digit !=="*") {
                if (checked.has(digit)) {
                    if (!repeat.has(digit)) {
                        repeat.set(digit, 2);
                    } else {
                        repeat.set(digit, repeat.get(digit) + 1);
                    }
                }
                checked.set(digit, true);
            }
        }

        return repeat;
    }
    function errorLines(repeat, type, number) {
        const output = [];
        repeat.forEach((count, digit) => {
            if (type === "region") {
                output.push(`in ${type} ${number} there are ${count} instances of ${digit}!`);
            } else {
                output.push(`in ${type} ${number} there are ${count} instances of ${digit}!`);
            }
        });
        return output;
    }

    let invalid = false;
    let output = [];
    for (let i = 0; i < n; i++) {
        const row = board[i];
        const col = [];
        for (let j = 0; j < n; j++) {
            col.push(board[j][i]);
        }
        const colRepeats = validate(col);

        const rowRepeats = validate(row);
        if (rowRepeats.size > 0) {
            invalid = true;
            output = output.concat(errorLines(rowRepeats, "row", i + 1));
        }
        if (colRepeats.size > 0) {
            invalid = true;
            output = output.concat(errorLines(colRepeats, "column", i + 1));
        }
    }

    // regions
    for (let startRow = 0; startRow < n; startRow += sqrtn) {
        for (let startCol = 0; startCol < n; startCol += sqrtn) {
            let region = [];
            for (let i = startRow; i < startRow + sqrtn; i++) {
                for (let j = startCol; j < startCol + sqrtn; j++) {
                    region.push(board[i][j]);
                }
            }

            const regionRepeats = validate(region);

            if (regionRepeats.size > 0) {
                invalid = true;
                let regionN = (startRow / sqrtn) * sqrtn + (startCol / sqrtn + 1);
                output = output.concat(errorLines(regionRepeats, "region", regionN));
            }
        }
    }

    if (invalid) {
        return ["sudoku is invalid.", ...output];
    } else {
        console.log("sudoku is valid.");
    }
}


let sudoku = [];
for (let i = 0; i < 9; i++) {
    let row = readline().split(" ");
    sudoku.push(row);}

let finalResult = CheckSudoku(sudoku);
finalResult.forEach((line) => {
    console.log(line);});

  
  