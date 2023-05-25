import React, { useState } from "react"

import styles from './DetailWorkout.module.scss'
import { EditWorkout } from "../edit/EditWorkout"
import { useWorkoutsContext } from "../../../services/contexts/WorkoutsContext"
import { Go } from "../go/Go"
import { deleteEl } from "../../../services/js/deleteEl"
import { useGlobalContext } from "../../../services/contexts/GlobalContext"


export const DetailWorkout = ({ 
  detailWorkout, setOpenDetail, setDetailWorkout, openEditExercise, setOpenEditExercise, 
  detailExercise, setDetailExercise
}) => {

  const [openEdit, setOpenEdit] = useState(false)
  const [openGo, setOpenGo] = useState(false)
 
  const {listWorkouts} = useWorkoutsContext()
  const {listGlobalPlaylists} = useGlobalContext()

  const [playlist, setPlaylist] = useState('None')

  return (
    <>
    {
      !openEdit && !openGo ? 
      <div className={styles.container}>
        <div className={styles.header}>
          <div onClick={() => setOpenDetail(false)} className={`icon-prev ${styles.icon}`} />
          <div onClick={() => setOpenEdit(true)} className={styles.edit}>
            <h3>Edit</h3>
            <div className={`icon-1 ${styles.icon}`} />
          </div>
        </div>
        <div className={styles.head}>
          <h2 className={styles.titleWorkout}>{detailWorkout.title}</h2>
          <div onClick={() => {
            deleteEl(listWorkouts, detailWorkout)
            setOpenDetail(false)
          }} className={`icon-delete ${styles.icon}`} />
        </div>
        <div className={styles.startWorkout}>
          <div className={styles.iconWorkout}>
            {detailWorkout.icon}
          </div>
          <button onClick={() => setOpenGo(true)} 
          className={styles.btnStart}>GO</button>
        </div>
        <div className={styles.playlists}>
          <select defaultValue={`${playlist}`}
            onChange={e => {
              setPlaylist(e.target.value)
              // Function for add playlist (reguest)
            }}
          >
            <option value={'None'}>None</option>
            {
              listGlobalPlaylists.map((playlist, index) => (
                <option value={`${playlist.title}`} key={index}>{playlist.title}</option>
              ))
            }
          </select>
        </div>
        <div className={styles.contentWorkout}>
          {
            detailWorkout.listExercises.map((exercise, index) => (
              <div key={index+1} className={styles.exercise}>
                <h4>Exercise {index+1} / Approaches: {exercise.listApproaches.length}</h4>
                <h3 className={styles.titleExercise}>{exercise.title}</h3>
                <div className={styles.listApproaches}>
                  {
                    exercise.listApproaches.map((approach, index) => (
                      <div key={index+1} className={styles.approach}>
                        <div className={styles.headApproach}>
                          <div className="icon-default" />
                          <h3 className={styles.countApp}>Approach {approach.count}</h3>
                        </div>
                        <div className={styles.bodyApproach}>
                          <div className={styles.parameter}>
                            <div className={styles.title}>
                              <div className="icon-1" />
                              <div className={styles.text}>Repeats</div>
                            </div>
                            <div className={styles.count}>{approach.mainParametr}</div>
                          </div>
                          <div className={styles.parameter}>
                            <div className={styles.title}>
                              <div className="icon-2" />
                              <div className={styles.text}>Weight</div>
                            </div>
                            <div className={styles.count}>{approach.weight} kg</div>
                          </div>
                          <div className={styles.parameter}>
                            <div className={styles.title}>
                              <div className="icon-3" />
                              <div className={styles.text}>Pause</div>
                            </div>
                            <div className={styles.count}>{approach.pause} sec</div>
                          </div>
                        </div>
                      </div>
                    ))
                  }
                </div>
              </div>
            ))
          }
        </div>
      </div>
      : openEdit ? <EditWorkout detailWorkout={detailWorkout} setOpenEdit={setOpenEdit} 
      setDetailWorkout={setDetailWorkout} openEditExercise={openEditExercise}
      setOpenEditExercise={setOpenEditExercise} detailExercise={detailExercise}
      setDetailExercise={setDetailExercise}
      />
      : openGo ? <Go workout={detailWorkout} setOpenGo={setOpenGo} />
      : null
    }
    </>
  )
}