function passPart1(truckLoads) {
    let n = 1e9 + 7;
    let s = 0;

    for (let i = 0; i < truckLoads.length; i++) {
      let smallest = truckLoads[i];
      s += smallest;

      for (let j = i + 1; j < truckLoads.length; j++) {
        smallest = Math.min(smallest, truckLoads[j]);
        s += smallest;
      }
      s %= n;
    }
    return s;
  }

function passPart2(truckNames) {
  const calculateScore = (truck, trucks) => trucks.filter(t => t.startsWith(truck)).length;

  const calculatePrice = (truck, trucks) => {
      let price = 0;
      for (let i = 0; i < truck.length; i++) {
          const start = truck.substring(0, i + 1);
          price += calculateScore(start, trucks);
      }
      return price;
  };

  // Calculate the total price of all trucks
  let totalPrice = 0;
  for (const truck of truckNames) {
      totalPrice += calculatePrice(truck, truckNames);
  }

  return totalPrice;
}

function passPart3(truckSpeeds) {
  const totalSum = truckSpeeds.reduce((a, b) => a + b, 0);
  let minDifference = Infinity;
  let splited = [];

  // Helper function to generate all subsets of an array
  const generateSubsets = (array) => {
    const subsets = [];
    const subsetCount = 1 << array.length; // 2^n possible subsets

    for (let i = 0; i < subsetCount; i++) {
      const subset = [];

      for (let j = 0; j < array.length; j++) {
        if ((i & (1 << j)) !== 0) {
          subset.push(array[j]);
        }
      }

      subsets.push(subset);
    }

    return subsets;
  };

  const allSubsets = generateSubsets(truckSpeeds);

  for (let subset of allSubsets) {
    const subsetSum = subset.reduce((a, b) => a + b, 0);
    const complementSum = totalSum - subsetSum;
    const difference = Math.abs(subsetSum - complementSum);

    if (difference < minDifference) {
      minDifference = difference;
      splited = [subsetSum, complementSum];
    }
  }
    let p1=splited[0]
    let p2=splited[1]
  return p1*p2;
}

let n = +readline();
let truckLoads = readline().split(" ").map(Number);
let truckNames = readline().split(" ");
let truckSpeeds = readline().split(" ").map(Number);

let  part1 = passPart1(truckLoads).toString();
let  part2 = passPart2(truckNames).toString();
let  part3 = passPart3(truckSpeeds).toString();
let  result = part1+part2+part3
console.log(result);
