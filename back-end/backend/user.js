import express  from 'express'
import {Response} from '../db/db.js'


const userRouter = express.Router()


// define the home page route
userRouter.get('/', async (req, res) => {
  const result = await Response.findAll()
  res.send(result)
})
// define the about route
userRouter.post('/', (req, res) => {
  console.log(req.body)
  res.send('post user')
})

export default userRouter