import React, { useState } from "react"

import { Exercises_html } from "./CreateExercises_html.jsx"
import { IconExercise } from "./IconExercise.jsx"
import { TypeExercise } from "./TypeExercise.jsx"


export const CreateExercises = ({ setOpenExercises, setListExercises }) => {

  const [openIcon, setOpenIcon] = useState(false)
  const [openType, setOpenType] = useState(false)

  const [idExercise, setIdExercise] = useState(undefined)
  const [titleExercise, setTitleExercise] = useState('')
  const [iconExercise, setIconExercise] = useState(
    <div className="icon-default" />
  )
  const [typeExercise, setTypeExercise] = useState('repeat')
  const [pauseExercise, setPauseExercise] = useState(30)
  const [listApproaches, setListApproaches] = useState([])

  const createExercise = () => {
    const newExercise = {
      id: idExercise,
      title: titleExercise,
      icon: iconExercise,
      type: typeExercise,
      pause: pauseExercise,
      listApproaches: listApproaches
    }

    const validation = () => {
      if (newExercise.title === undefined || newExercise.title === '') {
        alert('Enter the title')
      } else if (newExercise.listApproaches.length === 0) {
        alert('Add one approach')
      } else {
        setListExercises(prev => [...prev, newExercise])
        setOpenExercises(false)
      }
    }

    validation()
  }


  return (
    <>
    {
      !openIcon === true && !openType === true ?
      <Exercises_html setOpenIcon={setOpenIcon} setOpenType={setOpenType}
      setTitleExercise={setTitleExercise} titleExercise={titleExercise}
      iconExercise={iconExercise} setIconExercise={setIconExercise}
      typeExercise={typeExercise}
      listApproaches={listApproaches} setListApproaches={setListApproaches}
      setOpenExercises={setOpenExercises} createExercise={createExercise}
      pauseExercise={pauseExercise} setPauseExercise={setPauseExercise}
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