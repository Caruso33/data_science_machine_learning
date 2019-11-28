const mongoose = require("mongoose");
const validator = require("validator");

const dbUrl = "mongodb://127.0.0.1:27017";
const dbName = "mongoose";

mongoose.connect(`${dbUrl}/${dbName}`, {
  useNewUrlParser: true,
  useCreateIndex: true
});

const User = mongoose.model(
  "User",
  {
    name: {
      type: String,
      required: true,
      default: "John Doe"
    },
    age: {
      type: Number,
      validate(value) {
        // build-in
        if (value < 0) throw new Error("Age must be positive number");
      }
    },
    email: {
      type: String,
      required: true,
      unique: true,
      trim: true,
      lowercase: true,
      validate(value) {
        if (validator.isEmail(value)) throw new Error("Email is invalid");
      }
    },
    password: {
      type: String,
      required: true,
      minLength: 10,
      trim: true,
      validate(value) {
        if (value.includes("password"))
          throw new Error("Password cannot contain 'password'");
      }
    },
    active: {
      type: Boolean,
      default: true
    }
  },
  {
    timestamps: true
  }
);

const Task = mongoose.model("Task", {
  description: {
    type: String,
    required: true,
    trim: true
  },
  owner: {
    type: mongoose.Schema.Types.ObjectId,
    required: true,
    ref: "User"
  }
});

// later
// const task =  Task.findById('XYZ)
// await task.populate('owner').executePopulate()
// console.log(task)

// no ref stored on user, however still populatable
// userSchema.virtual('tasks', {
// ref: 'Task',
// localField: '_id', // user's id is refered on task.owner field
// foreignField: 'owner
// })

// check also instance methods
// user.pre('save', () => {function})

// check also schema methods
// userSchema.statics.functionXYZ = function
// userSchema.methods.functionXYZ = function

//
// CRUD
//

// CREATE
// insertOne();

// READ
// readAll();
// readById('5dd118d98eb9b514bcd513d1')
// readByProps({name: "Test0r"})

// UPDATE
// updateById('5dd118d98eb9b514bcd513d1',, {name: 'Test000r})
// updateByProps({name: "Test0r"}, {name: 'Test00r})

// DELETE
// deleteById('5dd118d98eb9b514bcd513d1')

function insertOne() {
  const user = new User({
    name: "Test0r",
    age: 123,
    email: "asdf",
    active: true
  });

  user
    .save()
    .then(() => console.log("user saved", user))
    .catch(err => console.log("unable to save user: ", err.message));
}

function readAll() {
  User.find({})
    .then(users => console.log("users found", users, User.countDocuments()))
    .catch(err => console.log("unable to find users: ", err.message));
}

function readById(id) {
  User.findById(id)
    .then(user => console.log("user found", user, User.countDocuments()))
    .catch(err => console.log("unable to find user: ", err.message));
}

function readByProps() {
  User.find({})
    .then(users => console.log("users found", users))
    .catch(err => console.log("unable to find users: ", err.message));
}

function updateById(id, props) {
  User.findByIdAndUpdate(id, props, { new: true, runValidators: true })
    // new: returned updated user, not old one,
    // runValidators: check that fields are properly set
    .then(user => console.log("user updated", user, User.countDocuments(props)))
    .catch(err => console.log("unable to find user: ", err.message));
}

function updateByProps(findProps, updateProps) {
  User.find(findProps, updateProps)
    .then(users => console.log("users updated", users))
    .catch(err => console.log("unable to find users: ", err.message));
}

function deleteById(id) {
  User.findByIdAndDelete(id)
    .then(user => console.log("user deleted", user, User.countDocuments(props)))
    .catch(err => console.log("unable to find user: ", err.message));
}
