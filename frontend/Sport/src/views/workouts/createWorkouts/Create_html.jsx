import React from "react"

import styles from './Create.module.scss'
import { Exercise } from "./Exercise";


export const Create_html = ({ setOpenCreate, setOpenIcon, setOpenExercises,
  titleWorkout, setTitleWorkout, iconWorkout, setIconWorkout, colorWorkout,
  setColorWorkout, createWorkout, listExercises, setListExercises,
  setOpenEditExercise, setDetailExercise
  }) => {


  return (
    <div className={styles.container}>
      <div className={styles.miniContainer}>
        <div className={styles.header}>
          <div onClick={() => setOpenCreate(false)} className={styles.back}>
            <div className="icon-prev" />
          </div>
          <h2>Create workout</h2>
        </div>
        <div className={styles.title}>
          <div onClick={() => setOpenIcon(true)} className={styles.logo}>
            {iconWorkout}
          </div>
          <form className={styles.form}>
            <div className={styles.formBody}>
              <input type="text" id="inputWorkout" placeholder="Title workout" 
                onChange={e => setTitleWorkout(e.target.value)}
                value={titleWorkout}            
              />
              <button onClick={() => setTitleWorkout('')} type="reset">
                <div className="icon-cancel" />
              </button>
            </div>
          </form>
        </div>
        <h3 className={styles.titleColor}>Color training in calendar</h3>
        <div className={styles.colors}>
          <div onClick={e => {
            setColorWorkout(getComputedStyle(e.target).backgroundColor)
            // console.log(getComputedStyle(e.target).backgroundColor);
            // console.log(colorWorkout.includes(getComputedStyle(e.target).backgroundColor));
            // colorWorkout.includes(getComputedStyle(e.target).backgroundColor) ? 
            // e.target.classList.contains('circ_1') : e.target.classList.remove('active')
          }} className={styles.circ_1} />
          <div onClick={e => setColorWorkout(getComputedStyle(e.target).backgroundColor)} className={styles.circ_2} />
          <div onClick={e => setColorWorkout(getComputedStyle(e.target).backgroundColor)} className={styles.circ_3} />
          <div onClick={e => setColorWorkout(getComputedStyle(e.target).backgroundColor)} className={styles.circ_4} />
          <div onClick={e => setColorWorkout(getComputedStyle(e.target).backgroundColor)} className={styles.circ_5} />
          <div onClick={e => setColorWorkout(getComputedStyle(e.target).backgroundColor)} className={styles.circ_6} />
          <div onClick={e => setColorWorkout(getComputedStyle(e.target).backgroundColor)} className={styles.circ_7} />
        </div>
        <div className={styles.createExercises}>
          <h3>Exercises</h3>
          <div className={styles.addExercise}>
            <h4>Add</h4>
            <div onClick={() => setOpenExercises(true)} className={styles.logo}>
              <div className="icon-add" />
            </div>
        </div>
      </div>
      </div>
      <div className={styles.listExerxises}>
        {
          listExercises.length === 0 ?
          <div className={styles.advice}>Add first exercise</div> :
          listExercises.map((exercise, index, listExercises) => (
            <Exercise key={index} exercise={exercise} setOpenEditExercise={setOpenEditExercise} 
            setDetailExercise={setDetailExercise}  listExercises={listExercises}
            />
          )) 
        }
      </div>
      <div className={styles.btn_container}>
        <button onClick={e => createWorkout(e)
        } className={styles.btn_create}>Create workout</button>
      </div>
      {/* <div className={styles.preview}>Add a first exercise</div> */}
    </div>
  )
}