import React, { useState } from "react"

import styles from './IconExercise.module.scss'


export const IconExercise = ({ setOpenIcon, IconExercise, setIconExercise }) => {

  const [icon, setIcon] = useState(IconExercise)

  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <div onClick={() => {
          setIcon(IconExercise)
          setOpenIcon(false)
        }} className={styles.cancel}>Cancel</div>
        <div onClick={() => {
          setIconExercise(icon)
          setOpenIcon(false)
        }} className={styles.ready}>Ready</div>
      </div>
      <div className={styles.finally_icon}>
        {icon}
      </div>
      <h3 className={styles.title_page}>Icon exercise</h3>
      <div className={styles.diving_line} />
      <div className={styles.icons_container}>
        <div onClick={() => setIcon(
            <div className="icon-1" />
          )} className={styles.icon}>
            <div className="icon-1" />
        </div>
        <div onClick={() => setIcon(
            <div className="icon-2" />
          )} className={styles.icon}>
            <div className="icon-2" />
        </div>
        <div onClick={() => setIcon(
            <div className="icon-3" />
          )} className={styles.icon}>
            <div className="icon-3" />
        </div>
        <div onClick={() => setIcon(
            <div className="icon-4" />
          )} className={styles.icon}>
            <div className="icon-4" />
        </div>
        <div onClick={() => setIcon(
            <div className="icon-5" />
          )} className={styles.icon}>
            <div className="icon-5" />
        </div>
        <div onClick={() => setIcon(
            <div className="icon-6" />
          )} className={styles.icon}>
            <div className="icon-6" />
        </div>
      </div>
    </div>
  ) 
}