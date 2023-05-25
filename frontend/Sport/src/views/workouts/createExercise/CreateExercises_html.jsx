import React, { useEffect, useState } from "react"

import styles from './CreateExercises.module.scss'
import { Approach } from './Approach.jsx'
// import { CreateService } from "../../../services/axios/workout.service"


export const Exercises_html = ({ titleExercise, setTitleExercise,
  setOpenIcon, setOpenType, iconExercise, listApproaches, 
  setListApproaches, createExercise, setOpenExercises, 
  typeExercise, pauseExercise, setPauseExercise
 }) => {

  const [countApp, setCountApp] = useState(1)

  const addApproach = () => {
    setCountApp(prev => prev + 1)
    const newApproach = {
      id: undefined,
      count: countApp,
      mainParametr: 10,
      weight: 25,
    }

    setListApproaches(prev => [...prev, newApproach])
  }

  return (
    <div className={styles.container}>
      <div className={styles.body}>
        <div className={styles.header}>
          <div onClick={() => setOpenExercises(false)} className={styles.cancel}>
            Cancel
          </div>
          <div className={styles.titlePage}>
            Add exericise
          </div>
          <div onClick={() => createExercise()} className={styles.ready}>
            Ready
          </div>
        </div>
        <div className={styles.titleExercise}>
          <div onClick={() => setOpenIcon(true)} className={styles.logo}>
            {iconExercise}
          </div>
          <form className={styles.form}>
            <div className={styles.formBody}>
              <input type="text" id="inputExercise" placeholder="Title exercise" 
                onChange={e => setTitleExercise(e.target.value)}
                value={titleExercise}
              />
              <button type="reset">
                <div className="icon-cancel" />
              </button>
            </div>
          </form>
        </div>
      </div>
      <div onClick={() => setOpenType(true)} className={styles.type}>
        <div className={styles.title}>Type exercise</div>
        <div className={styles.text}>
          <div className={styles.finally}>On {typeExercise}</div>
          <div className={`icon-next ${styles.icon}`} />
        </div>
      </div>
      <div className={styles.pause}>
        <div className={styles.title}>Pause beetwen approaches</div>
        <div className={styles.text}>
          <form className="form">
            <input type="text" 
              onChange={e => setPauseExercise(e.target.value)}
              value={pauseExercise} 
            />
          </form>
        </div>
      </div>
      <div className={styles.listApproach}>
        {
          listApproaches.map((approach, index) => (
              <Approach key={index+1} approach={approach} countApp={index+1} 
              typeExercise={typeExercise}
              />
            )
          )
        }
        <div onClick={addApproach}
        className={styles.addApproach}>Add approach</div>
      </div>
    </div>
  )
}