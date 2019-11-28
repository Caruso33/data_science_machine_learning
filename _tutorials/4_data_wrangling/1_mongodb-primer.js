const mongodb = require("mongodb");
const { ObjectID, MongoClient } = mongodb;
const faker = require("faker");

const dbUrl = "mongodb://127.0.0.1:27017";
const dbName = "mongo";
const collectionName = "users";

MongoClient.connect(dbUrl, { useNewUrlParser: true }, (err, client) => {
  if (err) {
    console.log("unable to connect to database");
    return process.exit(1);
  }

  const db = client.db(dbName);

  //   playWithIdsAndTimestamps();

  // CREATE
  //   insertOne(db);
  //   insertMany(db);

  // READ
  //   readOneWith_id(db);
  //   readOneWithName(db);
  //   readMany(db);

  // aggregate
  //   count(db);

  // UPDATE
  //   updateOne(db);

  // DELETE
  //   deleteOne(db);
  //   deleteMany(db);
});

function insertOne(db) {
  db.collection(collectionName).insertOne(
    {
      _id: playWithIdsAndTimestamps(),
      name: `Test0r`,
      email: faker.internet.email()
    },
    (err, result) => {
      if (err) console.log("unable to insert user");

      console.log(result.ops);
    }
  );
}

function insertMany(db) {
  db.collection(collectionName).insertMany(
    Array.from({ length: 20 }, (v, k) => ({
      name: `${faker.name.firstName()} ${faker.name.lastName()}`,
      email: faker.internet.email()
    })),
    (err, result) => {
      if (err) console.log("unable to insert many user");

      console.log(result.ops);
    }
  );
}

function playWithIdsAndTimestamps() {
  const id = new ObjectID();
  console.log("id", id, id.getTimestamp());

  return id;
}

function readOneWith_id(db) {
  db.collection(collectionName).findOne(
    { _id: new ObjectID("5dd110a460cfeb1206fd9e6b") },
    (err, result) => {
      if (err) console.log("unable to read user");

      console.log(result);
    }
  );
}

function readOneWithName(db) {
  db.collection(collectionName).findOne({ name: "Test0r" }, (err, result) => {
    if (err) console.log("unable to read user");

    console.log(result);
  });
}

function readMany(db) {
  db.collection(collectionName)
    .find({ name: "Test0r" }) // returns a cursor
    .toArray((err, result) => {
      if (err) console.log("unable to read users");

      console.log(result);
    });
}

function count(db) {
  db.collection(collectionName)
    .find({ name: "Test0r" }) // returns a cursor
    .count((err, result) => {
      if (err) console.log("unable to count users");

      console.log(result);
    });
}

function updateOne(db) {
  db.collection(collectionName)
    .updateOne(
      {
        //   _id: new Object('.....'),
        name: `Test0r`
      },
      {
        $set: {
          email: "testinat0r@gmail.com"
        }
      }
    )
    .then(result =>
      console.log(
        `matched: ${result.matchedCount}, updated: ${result.modifiedCount}`
      )
    )
    .catch(() => console.log("unable to update user"));
}

function deleteOne(db) {
  db.collection(collectionName)
    .deleteOne({
      _id: new Object("5dd10df8e137d5114753bebd")
      //   name: `Test0r`
    })
    .then(result => console.log(`deleted: ${result.deletedCount}`))
    .catch(() => console.log("unable to update user"));
}

function deleteMany(db) {
  db.collection(collectionName)
    .deleteMany({ name: `Test0r` })
    .then(result => console.log(`deleted: ${result.deletedCount}`))
    .catch(() => console.log("unable to update user"));
}
