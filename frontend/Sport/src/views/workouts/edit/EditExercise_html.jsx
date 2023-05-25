import React, { useState } from "react"

import styles from './EditExerice.module.scss'
import { Approach } from "../createExercise/Approach" 
import { deleteEl } from "../../../services/js/deleteEl"


export const EditExercises_html = ({ titleExercise, setTitleExercise,
  setOpenIcon, setOpenType, iconExercise, listApproaches, 
  setListApproaches, createExercise, setOpenEditExercise, 
  typeExercise, detailExercise, listExercises
 }) => {

  const [countApp, setCountApp] = useState(1)

  const addApproach = () => {
    setCountApp(prev => prev + 1)
    const newApproach = {
      count: countApp,
      mainParametr: 10,
      weight: 25,
      pause: 30,
    }
    setListApproaches(prev => [...prev, newApproach])
  }


  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <div onClick={() => setOpenEditExercise(false)} className={styles.cancel}>
          Cancel
        </div>
        <div onClick={() => {
          deleteEl(listExercises, detailExercise)
          setOpenEditExercise(false)
        }} 
          className={styles.delete}>
          Delete
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
      <div onClick={() => setOpenType(true)} className={styles.type}>
        <div className={styles.title}>Type exercise</div>
        <div className={styles.text}>
          <div>On {typeExercise}</div>
          <div className="icon-next" />
        </div>
      </div>
      <div className={styles.listApproach}>
        {
          listApproaches.map((approach, index) => (
              <Approach key={index+1} approach={approach} countApp={index+1} listApproaches={listApproaches} />
            )
          )
        }
        <div onClick={addApproach}
        className={styles.addApproach}>Add approach</div>
      </div>
    </div>
  )
}