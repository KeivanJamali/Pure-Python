function count_Dots(material) {
  const persianLetters = {
    'ا': 0,
    'ب': 1,
    'پ': 3,
    'ت': 2,
    'ث': 3,
    'ج': 1,
    'چ': 3,
    'ح': 0,
    'خ': 1,
    'د': 0,
    'ذ': 1,
    'ر': 0,
    'ز': 1,
    'ژ': 3,
    'س': 0,
    'ش': 3,
    'ص': 0,
    'ض': 1,
    'ط': 0,
    'ظ': 1,
    'ع': 0,
    'غ': 1,
    'ف': 1,
    'ق': 2,
    'ک': 0,
    'گ': 0,
    'ل': 0,
    'م': 0,
    'ن': 1,
    'و': 0,
    'ه': 0,
    'ی': 0,
  };

  const englishLetters = {
    uppercase: {
      'A': 0,
      'B': 0,
      'C': 0,
      'D': 0,
      'E': 0,
      'F': 0,
      'G': 0,
      'H': 0,
      'I': 0,
      'J': 0,
      'K': 0,
      'L': 0,
      'M': 0,
      'N': 0,
      'O': 0,
      'P': 0,
      'Q': 0,
      'R': 0,
      'S': 0,
      'T': 0,
      'U': 0,
      'V': 0,
      'W': 0,
      'X': 0,
      'Y': 0,
      'Z': 0
    },
    lowercase: {
      'a': 0,
      'b': 0,
      'c': 0,
      'd': 0,
      'e': 0,
      'f': 0,
      'g': 0,
      'h': 0,
      'i': 1,
      'j': 1,
      'k': 0,
      'l': 0,
      'm': 0,
      'n': 0,
      'o': 0,
      'p': 0,
      'q': 0,
      'r': 0,
      's': 0,
      't': 0,
      'u': 0,
      'v': 0,
      'w': 0,
      'x': 0,
      'y': 0,
      'z': 0
    }
  };
    let dots = 0;
    for (let j = 0; j < material.length; j++) {
      if (englishLetters.uppercase.hasOwnProperty(material[j])) {
        dots += englishLetters.uppercase[material[j]];
      } else if (englishLetters.lowercase.hasOwnProperty(material[j])) {
        dots += englishLetters.lowercase[material[j]];
      } else if (persianLetters.hasOwnProperty(material[j])) {
        if (material[j] === 'ی' && material[j + 1] !== ' ' && j != (material.length - 1)) {
          dots += 2;
        } else {
          dots += persianLetters[material[j]];
        }
      }
    }

  return dots}



let n = parseInt(readline());

for (let i = 0; i < n; i++) {
    const material = readline();
    console.log(count_Dots(material));
}

// const readline = require('readline');
// const rl = readline.createInterface({
//   input: process.stdin,
//   output: process.stdout
// });

// rl.question('', (n) => {
//   const wordCounts = [];

//   function processInput() {
//     if (n > 0) {
//       rl.question('', (material) => {
//         const dotCount = count_Dots(material);
//         wordCounts.push(dotCount);
//         n--;
//         processInput();
//       });
//     } else {
//       rl.close();
//       wordCounts.forEach((count) => {
//         console.log(count);
//       });
//     }
//   }

//   processInput();
// });