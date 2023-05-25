import React from "react"

import styles from './Workout.module.scss'


export const Workout = ({ workout, setOpenDetail, setDetailWorkout }) => {

  return (
    <div className={styles.workout}>
      <div onClick={() => {
        setDetailWorkout(workout)
        setOpenDetail(true)
        }} className={styles.body}>
        <div className={styles.logo}>
          {workout.icon}
        </div>
        <div className={styles.text}>
          <h3>{workout.title}</h3>
          <div className={styles.exercise}>Exercises: {workout.listExercises.length}</div>
        </div>
      </div>
      <div className={styles.icons}>
        <div className={styles.more}>
          <div className="icon-next" />
        </div>
      </div>     
    </div>
  )
}