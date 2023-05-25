import React from "react"

import styles from "./EditWorkout.module.scss"
import { Exercise } from "../createWorkouts/Exercise"


export const EditWorkout_html = ({ setOpenEdit, setOpenIcon, setOpenExercises,
  titleWorkout, setTitleWorkout, iconWorkout, setIconWorkout, colorWorkout,
  setColorWorkout, createWorkout, listExercises, setListExercises, setDetailExercise,
  setOpenEditExercise
  }) => {


  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <div onClick={() => setOpenEdit(false)} className={styles.back}>
          <div className="icon-prev" />
        </div>
        <h2>Edit workout</h2>
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
            <button type="reset">
              <div className="icon-cancel" />
            </button>
          </div>
        </form>
      </div>
      <h3 className={styles.titleColor}>Color training in calendar</h3>
      <div className={styles.colors}>
        <div onClick={(e) => setColorWorkout(getComputedStyle(e.target).backgroundColor)} className={styles.circ_1} />
        <div onClick={(e) => setColorWorkout(getComputedStyle(e.target).backgroundColor)} className={styles.circ_2} />
        <div onClick={(e) => setColorWorkout(getComputedStyle(e.target).backgroundColor)} className={styles.circ_3} />
        <div onClick={(e) => setColorWorkout(getComputedStyle(e.target).backgroundColor)} className={styles.circ_4} />
        <div onClick={(e) => setColorWorkout(getComputedStyle(e.target).backgroundColor)} className={styles.circ_5} />
        <div onClick={(e) => setColorWorkout(getComputedStyle(e.target).backgroundColor)} className={styles.circ_6} />
        <div onClick={(e) => setColorWorkout(getComputedStyle(e.target).backgroundColor)} className={styles.circ_7} />
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
      <div className={styles.listExerxises}>
        {
          listExercises.map((exercise, index) => (
            <Exercise key={index} exercise={exercise} setDetailExercise={setDetailExercise} 
            setOpenEditExercise={setOpenEditExercise}
            />
          ))
        }
      </div>
      <div className={styles.btn_container}>
        <button onClick={e => createWorkout(e)
        } className={styles.btn_create}>Save</button>
      </div>
      {/* <div className={styles.preview}>Add a first exercise</div> */}
    </div>
  )
}