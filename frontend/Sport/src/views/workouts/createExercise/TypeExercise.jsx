import React from "react"

import styles from './TypeExercise.module.scss'


export const TypeExercise = ({ setOpenType, setTypeExercise }) => {


  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <div onClick={() => setOpenType(false)} className={styles.back}>
          <div className="icon-prev" />
        </div>
        <h2 className={styles.titlePage}>Choose type of exercise</h2>
      </div>
      <div onClick={() => {
        setTypeExercise('repeat')
        setOpenType(false)
      }} className={styles.type}>
        For a repeat
      </div>
      <div className={styles.description}>
        Approach continue, while you don't choose by you count 
        of repetitions, for example, 10 push-up
      </div>
      <div onClick={() => {
        setTypeExercise('time')
        setOpenType(false)
      }} className={styles.type}>
        For a time
      </div>
      <div className={styles.description}>
        Approach continue, while will run out choose by you time,
        for example, stand of rack for 30 seconds
      </div>
    </div>
  ) 
}