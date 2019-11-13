const faker = require("faker");
const mysql = require("mysql");
const express = require("express");
const bodyParser = require("body-parser");

let connection,
  app,
  PORT = process.env.PORT || 8080;

function connectDB() {
  connection = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "password",
    database: "sql_course_web_app"
  });

  connection.connect();
}

function runQuery(query, data, cb) {
  return connection.query(query, data, (err, results) => {
    if (err) throw err;

    if (cb) cb(results);
    else console.log(results);
  });
}

function startExpress() {
  app = express();

  app.set("view engine", "ejs");
  app.use(bodyParser.urlencoded({ extended: true }));
  app.use(express.static(__dirname + "/views"));

  app.get("/", (req, res) => {
    runQuery("SELECT COUNT(*) AS count FROM users", null, result => {
      const count = result[0].count;
      res.render("home", { count });
    });
  });

  app.post("/register", (req, res) => {
    var person = { email: req.body.email };
    runQuery("INSERT INTO users SET ?", person, result => {
      console.log(result);
      res.redirect("/");
    });
  });

  app.listen(PORT, () => {
    console.log("App listening on: ", PORT);
  });
}

async function run() {
  connectDB();

  await runQuery("SELECT COUNT(*) AS count FROM users", null, result => {
    if (result[0].count < 600) return seed();
  });

  startExpress();

  // connection.end()
}

run();

async function seed() {
  let users = [];
  for (let i = 0; i < 500; i++) {
    users.push([faker.internet.email(), faker.date.past()]);
  }
  return runQuery(
    "INSERT INTO users (email, created_at) VALUES ?",
    [users],
    result => console.log("seeding result: ", result)
  );
}
