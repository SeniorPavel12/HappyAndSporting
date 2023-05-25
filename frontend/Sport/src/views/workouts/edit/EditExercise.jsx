import React, { useState } from "react"

import { IconExercise } from "../createExercise/IconExercise.jsx"
import { TypeExercise } from "../createExercise/TypeExercise.jsx" 
import { EditExercises_html } from "./EditExercise_html.jsx"


export const EditExercise = ({ 
  detailExercise, setListExercises, listExercises, setOpenEditExercise 
}) => {

  const func = (listWorkouts, workout) => {
    listWorkouts.splice(listWorkouts.indexOf(workout), 1)
  }

  const [openIcon, setOpenIcon] = useState(false)
  const [openType, setOpenType] = useState(false)

  const [titleExercise, setTitleExercise] = useState(detailExercise.title)
  const [iconExercise, setIconExercise] = useState(detailExercise.icon)
  const [typeExercise, setTypeExercise] = useState(detailExercise.type)
  const [listApproaches, setListApproaches] = useState(detailExercise.listApproaches)

  const createExercise = () => {
    const newExercise = {
      title: titleExercise,
      icon: iconExercise,
      type: typeExercise,
      listApproaches: listApproaches
    }

    const validation = () => {
      if (newExercise.title === undefined || newExercise.title === '') {
        alert('Enter the title')
      } else if (newExercise.listApproaches.length === 0) {
        alert('Add one approach')
      } else {
        func(listExercises, detailExercise)
        setListExercises(prev => [...prev, newExercise])
        setOpenEditExercise(false)
      }
    }

    validation()
  }

  return (
    <>
    {
      !openIcon === true && !openType === true ?
      <EditExercises_html setOpenIcon={setOpenIcon} setOpenType={setOpenType}
      setTitleExercise={setTitleExercise} titleExercise={titleExercise}
      iconExercise={iconExercise} setIconExercise={setIconExercise}
      typeExercise={typeExercise}
      listApproaches={listApproaches} setListApproaches={setListApproaches}
      setOpenEditExercise={setOpenEditExercise} createExercise={createExercise}
      listExercises={listExercises} detailExercise={detailExercise}
      />
      : openIcon === true ? <IconExercise setOpenIcon={setOpenIcon}
      iconExercise={iconExercise} setIconExercise={setIconExercise}
      />
      : openType === true ? <TypeExercise setOpenType={setOpenType}
      setTypeExercise={setTypeExercise}
      />
      : null
    }
    </> 
  )
}