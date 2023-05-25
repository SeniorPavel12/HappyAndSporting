import React, { useState } from 'react'

import styles from './Registration.module.scss'
import { LoginService } from '../../services/axios/login.service'


export const Registration = ({ setOpenRegister, setOpenEntry }) => {
  
  const [login, setLogin] = useState('')
  const [pass, setPass] = useState('')

  const register = async () => {
    const data = await LoginService.createUsers(login, pass)

    setOpenRegister(false)
    setLogin(true)
  }
  
  return (
    <div className={styles.container}>
      <h2 className={styles.titlePage}>Resitration</h2>
      <form action="#" className='form'>
        <div className={styles.formItem}>
          <label htmlFor="formLogin" className={styles.formLabel}>Login:</label>
          <input type="text" id="formLogin" name="login" className={styles.formInput}
          onChange={e => setLogin(e.target.value)} value={login}
          />
        </div>
        <div className={styles.formItem}>
          <label htmlFor="formPass" className={styles.formLabel}>Password:</label>
          <input type="text" id="formPass" name="pass" className={styles.formInput}
          onChange={e => setPass(e.target.value)} value={pass}
          />
        </div>
        <button onClick={register} type='reset' className={styles.btn}>Entry</button>
      </form>
    </div>
  )
}