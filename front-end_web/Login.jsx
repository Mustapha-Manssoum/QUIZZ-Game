/*
import React, { useState } from "react";
import { Link } from "react-router-dom";
export const Login = (props)=>{
    const [email,setEmail] = useState('');
    const [pass,setPass] = useState('');


    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(email);
        


    }


        return (
        <div className="auth-form-container">
           <h2>Login</h2>
           <form className="login-form" onSubmit = {handleSubmit}>
               <label htmlfor="email">email</label>
               <input value={email} type="email" placeholder="youremail@gmail.com" id="email" name="email" />


                <label htmlfor="password">password</label>
                <input value={email} type="password" placeholder="***********" id="password" name="password" />

                <button className= "link-btn" onClick={() => props.onFormSwitch('register')}  type="submit"> Log In </button>
           </form>
        <button className= "link-btn" onClick={() => props.onFormSwitch('register')}> Dont't have have an account ? Register here </button>
        </div>

    )


    

    
} 
*/
import React, { useState } from "react";
import { useHistory } from 'react-router-dom';



export const Login = (props) => {
    const [email, setEmail] = useState('');
    const [pass, setPass] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(email);
    }

    return (
        <div className="auth-form-container">
            <h2>Login</h2>
            <form className="login-form" onSubmit={handleSubmit}>
                <label htmlFor="email">email</label>
                <input value={email} onChange={(e) => setEmail(e.target.value)}type="email" placeholder="youremail@gmail.com" id="email" name="email" />
                <label htmlFor="password">password</label>
                <input value={pass} onChange={(e) => setPass(e.target.value)} type="password" placeholder="********" id="password" name="password" />
                <button className="link-btn" onClick={() => props.onFormSwitch('Quiz')} type="submit" >Log In</button>
                
            </form>
            <button className="link-btn" onClick={() => props.onFormSwitch('register')}>Don't have an account? Register here.</button>
        </div>
    )
}