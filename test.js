/* test.js */

"use strict";

// Add file system module
const fs = require("fs");

// Training data path
const dataFolderPath = "res/data/";

function getDirectoryContents(directoryPath) {
  return new Promise((resolve, reject) => {
      fs.readdir(dataFolderPath, (err, files) => {
        resolve(files);
      });
  });
}

function getFileContents(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, "utf8", (err, data) => {
      if (err) { reject(err); }
      resolve(data);
    });
  });
}

function parseData() {

}

function main() {

  //let getDataPromise = 
  getDirectoryContents(dataFolderPath).then(
    (files) => {
      files.forEach(file => {
        let filePath = dataFolderPath + file;
        getFileContents(filePath); 
      });
    }
  );

  //let parseDataPromise = new Promise(...);

  // Train on data
  /*
  getDataPromise.then(
    (data) => {
      console.log(data);
      //parseDataPromise(data)
    }
  );
  */
}

main();
