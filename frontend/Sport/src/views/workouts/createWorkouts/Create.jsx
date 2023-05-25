import React, { useState } from "react"

import { useWorkoutsContext } from "../../../services/contexts/WorkoutsContext"
import { IconWorkout } from "./IconWorkout"
import { CreateExercises } from "../createExercise/CreateExercises"
import { Create_html } from './Create_html'
import { EditExercise } from "../edit/EditExercise"
import { WorkoutService } from "../../../services/axios/workout.service"
import { ExerciseService } from "../../../services/axios/exericise.service"
import { ApproachService } from "../../../services/axios/approach.service"


export const Create = ({ 
  setOpenCreate, openEditExercise, setOpenEditExercise, detailExercise, setDetailExercise
}) => {

  const {toggle} = useWorkoutsContext()

  const [openIcon, setOpenIcon] = useState(false)
  const [openExercises, setOpenExercises] = useState(false)

  const [idWorkout, setIdWorkout] = useState(undefined)
  const [titleWorkout, setTitleWorkout] = useState('')
  const [iconWorkout, setIconWorkout] = useState(
    <div className="icon-default" />
  )
  const [colorWorkout, setColorWorkout] = useState('rgb(38, 70, 83)')
  const [listExercises, setListExercises] = useState([])

  const createWorkout = (e) => {
    e.preventDefault()
    const newWorkout = {
      id: idWorkout,
      title: titleWorkout,
      icon: iconWorkout,
      color: colorWorkout,
      listExercises: listExercises
    }

    // const createWorkout = async () => {
    //   const data = await WorkoutService.create({
    //     name: newWorkout.title,
    //     color: newWorkout.color,
    //     icon: newWorkout.icon,
    //     initial_break: 10,
    //     playlist: ""
    //   })
    //   setIdWorkout(data)
    // }

    // const createExercise = async (exercise, index) => {
    //   const data = await ExerciseService.create({
    //     name: exercise.title,
    //     icon: exercise.icon,
    //     type: exercise.type,
    //     number: index,
    //     break_between_approaches: exercise.pause,
    //     break_after_exercise: 30,
    //     workout: newWorkout
    //   })
    //   exercise.id = data
    // }

    // const createApproach = async (approach, index, exercise) => {
    //   const data = await ApproachService.create({
    //     newWorkout: approach.weight,
    //     repetitions: exercise.type === 'repeat' ? approach.mainParametr : "",
    //     duration: exercise.type === 'time' ? approach.mainParametr : "",
    //     number: index,
    //     exercise: exercise
    //   })
    //   approach.id = data
    // }

    const validation = () => {
      if (newWorkout.title === undefined || newWorkout.title === '') {
        alert('Enter the title')
      } else if (newWorkout.listExercises.length === 0) {
        alert('Add one exercise')
      } else {
        // funcRequest()
        toggle(newWorkout)
        setOpenCreate(false)
        // createWorkout()
        // for (let i = 1; i <= newWorkout.listExercises; i++) {
        //   createExercise(newWorkout.listExercises[i], i)
        //   for (let j = 1; j <= newWorkout.listExercises[i].listApproaches[j]; j++) {
        //     createApproach(newWorkout.listExercises[i].listApproaches[j], j, newWorkout.listExercises[i])
        //   }
        // }
      }
    }

    validation()
  }

  return (
    <>
    {
      !openIcon && !openExercises && !openEditExercise ?
      <Create_html setOpenCreate={setOpenCreate} setOpenIcon={setOpenIcon}
      setOpenExercises={setOpenExercises} 
      titleWorkout={titleWorkout} setTitleWorkout={setTitleWorkout}
      iconWorkout={iconWorkout} setIconWorkout={setIconWorkout}
      colorWorkout={colorWorkout} setColorWorkout={setColorWorkout}
      createWorkout={createWorkout} listExercises={listExercises}
      setListExercises={setListExercises} setOpenEditExercise={setOpenEditExercise}
      setDetailExercise={setDetailExercise}
      />
      : openIcon ? <IconWorkout setOpenIcon={setOpenIcon} 
      iconWorkout={iconWorkout} setIconWorkout={setIconWorkout} 
      />
      : openExercises ? <CreateExercises setOpenExercises={setOpenExercises}
      setListExercises={setListExercises}
      />
      : openEditExercise ? <EditExercise detailExercise={detailExercise} 
      setListExercises={setListExercises} setOpenEditExercise={setOpenEditExercise}
      listExercises={listExercises}
      />
      : null
    }
    </>
  )
}