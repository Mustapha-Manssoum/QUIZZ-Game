import express from 'express';
import questionRouter from './question.js'
import userRouter from './user.js'
import cors from 'cors'


const app = express()
app.use(express.json())
app.use(cors())


app.use('/question', questionRouter)
app.use('/user', userRouter)

app.listen(3033, ()=>console.log('Start server'))