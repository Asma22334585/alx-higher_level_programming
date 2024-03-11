#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const nums = process.argv.slice(2);
  nums.sort((x, y) => y - x);
  console.log(nums[1]);
}
