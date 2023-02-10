import {DataTypes, Sequelize} from 'sequelize'
import dotenv from 'dotenv';

dotenv.config();

const DB_NAME = process.env.DB_NAME
const DB_HOST = process.env.DB_HOST
const DB_USER = process.env.DB_USER
const DB_PASSWORD = process.env.DB_PASSWORD
const DB =  new Sequelize(DB_NAME, DB_USER, DB_PASSWORD, {dialect: 'mysql', host: DB_HOST})

const Question = DB.define('Question',{
    id : {
        type: DataTypes.INTEGER.UNSIGNED,
        primaryKey:  true,
        autoIncrement: true,
        allowNull: false
    },
    questionText : {
        type: DataTypes.STRING,
        allowNull: false
    },
    correctResponse: {
        type: DataTypes.INTEGER.UNSIGNED,
        allowNull: false
    },
    category: {
        type: DataTypes.STRING,
        allowNull: false
    }
},{timestamps:false})

const Response = DB.define('Response',{
    id : {
        type: DataTypes.INTEGER.UNSIGNED,
        primaryKey:  true,
        autoIncrement: true,
        allowNull: false
    },
    ResponseText : {
        type: DataTypes.STRING,
        allowNull: false
    },
    
},{timestamps:false})

Question.Responses = Question.hasMany(Response, {
    onDelete: 'CASCADE',
    foreignKey: {
        allowNull: false
    }
})
Response.Question = Response.belongsTo(Question)


DB.sync()
//.then(() => DB.drop())
.then(() => {
    console.log("db connected")
})
.catch(error => console.log("DB KO: ", error))

export {DB, Response, Question}