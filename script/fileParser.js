const data = require("./data.json");
const fs = require("fs");

let newData = {};

data.forEach((item) => {
  const { t, ...restOfItem } = item;

  newData = { ...newData, [t]: restOfItem };
});

const jsonString = JSON.stringify(newData, null, 2);

try {
  fs.writeFileSync("formatted.json", jsonString);
  console.log("Data written to file");
} catch (err) {
  console.error("Error writing file:", err);
}
