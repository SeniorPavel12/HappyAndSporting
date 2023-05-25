import React, { useState } from "react"

import { EditWorkout_html } from "./EditWorkout_html"
import { IconWorkout } from "../createWorkouts/IconWorkout"
import { CreateExercises } from "../createExercise/CreateExercises"
import { useWorkoutsContext } from "../../../services/contexts/WorkoutsContext"
import { EditExercise } from "./EditExercise"
import { deleteEl } from "../../../services/js/deleteEl"
import { WorkoutService } from "../../../services/axios/workout.service"
import { ExerciseService } from "../../../services/axios/exericise.service"
import { ApproachService } from "../../../services/axios/approach.service"


export const EditWorkout = ({ 
  detailWorkout, setOpenEdit, setDetailWorkout, openEditExercise, setOpenEditExercise, 
  detailExercise, setDetailExercise
}) => {

  const {toggle} = useWorkoutsContext()

  const {listWorkouts} = useWorkoutsContext()

  const [openIcon, setOpenIcon] = useState(false)
  const [openExercises, setOpenExercises] = useState(false)

  const [idWorkout, setIdWorkout] = useState(detailWorkout.id)
  const [titleWorkout, setTitleWorkout] = useState(detailWorkout.title)
  const [iconWorkout, setIconWorkout] = useState(detailWorkout.icon)
  const [colorWorkout, setColorWorkout] = useState(detailWorkout.color)
  const [listExercises, setListExercises] = useState(detailWorkout.listExercises)

  const createWorkout = (e) => {
    e.preventDefault()
    const newWorkout = {
      id: idWorkout,
      title: titleWorkout,
      icon: iconWorkout,
      color: colorWorkout,
      listExercises: listExercises
    }

    // const editWorkout = async () => {
    //   const data = await WorkoutService.edit({
    //     name: newWorkout.title,
    //     color: newWorkout.color,
    //     icon: newWorkout.icon,
    //     initial_break: 10,
    //     playlist: ""
    //   })
    // }

    // const editExercise = async (exercise, index) => {
    //   const data = await ExerciseService.edit({
    //     name: exercise.title,
    //     icon: exercise.icon,
    //     type: exercise.type,
    //     number: index,
    //     break_between_approaches: exercise.pause,
    //     break_after_exercise: 30,
    //     workout: newWorkout
    //   })
    // }

    // const editApproach = async (approach, index, exercise) => {
    //   const data = await ApproachService.create({
    //     newWorkout: approach.weight,
    //     repetitions: exercise.type === 'repeat' ? approach.mainParametr : "",
    //     duration: exercise.type === 'time' ? approach.mainParametr : "",
    //     number: index,
    //     exercise: exercise
    //   })
    // }

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
        deleteEl(listWorkouts, detailWorkout)
        toggle(newWorkout)
        setDetailWorkout(newWorkout)
        setOpenEdit(false)
        // editWorkout()
        // for (let i = 1; i <= newWorkout.listExercises; i++) {
        //   if (newWorkout.listExercises[i] !== undefined) {
        //     editExercise(newWorkout.listExercises[i], i)
        //   } else {
        //     createExercise(newWorkout.listExercises[i], i)
        //   }
        //   for (let j = 1; j <= newWorkout.listExercises[i].listApproaches[j]; j++) {
        //     if (newWorkout.listExercises[i].listApproaches[j] !== undefined) {
        //       editApproach(newWorkout.listExercises[i].listApproaches[j], j, newWorkout.listExercises[i])
        //     } else {
        //       createApproach(newWorkout.listExercises[i].listApproaches[j], j, newWorkout.listExercises[i])
        //     }
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
      <EditWorkout_html setOpenEdit={setOpenEdit} setOpenIcon={setOpenIcon}
      setOpenExercises={setOpenExercises} 
      titleWorkout={titleWorkout} setTitleWorkout={setTitleWorkout}
      iconWorkout={iconWorkout} setIconWorkout={setIconWorkout}
      colorWorkout={colorWorkout} setColorWorkout={setColorWorkout}
      createWorkout={createWorkout} listExercises={listExercises}
      setListExercises={setListExercises} setDetailExercise={setDetailExercise}
      setOpenEditExercise={setOpenEditExercise}
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