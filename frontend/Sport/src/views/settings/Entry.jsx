import React from 'react'

import styles from './Entry.module.scss'
import { LoginService } from '../../services/axios/login.service'


export const Entry = ({ setOpenEntry }) => {

  const [login, setLogin] = useState('')
  const [pass, setPass] = useState('')
  
  return (
    <div className={styles.container}>
      <h2 className={styles.titlePage}>Entry</h2>
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
        <button onClick={() => LoginService.logoutUser()} type='reset' className={styles.btn}>Entry</button>
      </form>
    </div>
  )
}