import React, { useState } from "react";

import styles from './ListWorkouts.module.scss'
import { Navigation } from '/src/components/display/Navigation.jsx'
import { useWorkoutsContext } from "../../../services/contexts/WorkoutsContext";
import { Workout } from "./Workout";


export const ListWorkouts = ({
  setOpenCreate, setOpenDetail, setDetailWorkout 
}) => {

  const {listWorkouts} = useWorkoutsContext({})
  
  
  return (
    <>
    <div className={styles.container}>
        <div onClick={() => setOpenCreate(true)} className={styles.addWorkout}>
          <h4>Add</h4>
          <div className={styles.logo}>
            <div className="icon-add" />
          </div>
        </div>
      <h1>Workouts</h1>
      <div className={styles.listWorkout}>
        {
          listWorkouts.map((workout, index) => (
            <Workout key={index} workout={workout} setOpenDetail={setOpenDetail}
            setDetailWorkout={setDetailWorkout}
            />
          ))
        }
      </div>
    </div>
    <Navigation />
    </>
  )
}