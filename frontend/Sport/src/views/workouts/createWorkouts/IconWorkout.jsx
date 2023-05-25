import React, { useState } from "react"

import styles from './IconWorkout.module.scss'


export const IconWorkout = ({ setOpenIcon, iconWorkout, setIconWorkout }) => {

  const [icon, setIcon] = useState(iconWorkout)

  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <div onClick={() => {
          setIcon(iconWorkout)
          setOpenIcon(false)
        }} className={styles.cancel}>Cancel</div>
        <div onClick={() => {
          setIconWorkout(icon)
          setOpenIcon(false)
        }} className={styles.ready}>Ready</div>
      </div>
      <div className={styles.finally_icon}>
        {icon}
      </div>
      <h3 className={styles.title_page}>Icon workout</h3>
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