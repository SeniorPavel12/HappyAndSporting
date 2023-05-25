import React, { useState } from "react"

import { ListWorkouts } from './workouts/listWorkouts/ListWorkouts'
import { WorkoutsProvider } from "../services/contexts/WorkoutsContext"
import { Create } from "./workouts/createWorkouts/Create"
import { DetailWorkout } from "./workouts/detail/DetailWorkout"


export const App = () => {

  const [openCreate, setOpenCreate] = useState(false)
  const [openDetail, setOpenDetail] = useState(false)
  const [openEditExercise, setOpenEditExercise] = useState(false)

  const [detailWorkout, setDetailWorkout] = useState()
  const [detailExercise, setDetailExercise] = useState()
  
  return (
    <>
    <div className="myContainer">
      <WorkoutsProvider>
        {
          !openCreate && !openDetail ? 
          <ListWorkouts setOpenCreate={setOpenCreate} setOpenDetail={setOpenDetail} 
          setDetailWorkout={setDetailWorkout}
          />
          : openCreate ? <Create setOpenCreate={setOpenCreate} 
          openEditExercise={openEditExercise} setOpenEditExercise={setOpenEditExercise}
          detailExercise={detailExercise} setDetailExercise={setDetailExercise}
          /> 
          : openDetail ? <DetailWorkout detailWorkout={detailWorkout} 
          setOpenDetail={setOpenDetail} setDetailWorkout={setDetailWorkout}
          openEditExercise={openEditExercise} setOpenEditExercise={setOpenEditExercise}
          detailExercise={detailExercise} setDetailExercise={setDetailExercise}
          />
          : null
        }
      </WorkoutsProvider>
    </div>
    <h1 className="limition">Please, change device</h1>
    </>
  )
}