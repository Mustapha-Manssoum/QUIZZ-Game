import express  from 'express'
import {Question,Response} from '../db/db.js'

const questionRouter = express.Router()


// define the home page route
questionRouter.get('/', async (req, res) => {
  const category = req.query.category
  let questions = await Question.findAll({include: Response})
  if(category) {
    questions = questions.filter(question => question.category === category)
  }
  res.status(200).send(questions)
})
// define the about route
questionRouter.post('/', async (req, res) => {
    const question = req.body.question;
    const responses = req.body.responses;
    const newQuestion = await Question.create({
      questionText: question.questionText,
      correctResponse: parseInt(question.correctResponse),
      category: question.category,
      Responses: responses
    },{include: [Response]}) 
  res.status(201).send(newQuestion)
})

export default questionRouter
