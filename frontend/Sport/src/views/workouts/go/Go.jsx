import React, { useState } from "react"

import { Go_html } from "./Go_html"


export const Go = ({ workout, setOpenGo }) => {

  const [data, setData] = useState({
    weight: 0,
    repetitions: 0,
    duration: 0,
    titleExercise: '',
    countApp: 0,
  })

  const [nextData, setNextData] = useState({
    weight: 0,
    repetitions: 0,
    duration: 0,
    titleExercise: '',
    countApp: 0,
  })

  const [time, setTime] = useState(10)
  const [allApp, setAllApp] = useState(0)
  const [event, setEvent] = useState('init')


  // const socket = new WebSocket("ws://javascript.info");

  // socket.onopen = () => {
  //   socket.send({"type": "SW", "workout": `${workout.id}`})
  // }

  // socket.onmessage = (e) => {
  //   const message = JSON.parse(e.data)
  //   setTime(message.data.time)
  //   setAllApp(message.other_data.count_all_approach)
  //   setNextData(...{
  //     weight: message.data.working_weight,
  //     repetitions: message.data.repetitions,
  //     duration: message.data.duration,
  //     titleExercise: message.other_data.name_exercise,
  //     countApp: message.other_data.count_exercise,
  //   })
  // }


  return (
    <Go_html workout={workout} setOpenGo={setOpenGo} 
    />
  )
}