import React, { useEffect, useState } from 'react'

import styles from './Go.module.scss'


export const Go_html = ({ workout, setOpenGo }) => {

  
  const [ seconds, setSeconds ] = useState(60);
  const [ timerActive, setTimerActive ] = useState(true);

  useEffect(() => {
    if (seconds > 0 && timerActive) {
      setTimeout(setSeconds, 1000, seconds - 1);
    } else {
      setTimerActive(false);
    }
  }, [ seconds, timerActive ]);


  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <div className={styles.titlePage}>
          <h4 className={styles.titleWorkout}>
            {workout.title}
          </h4>
          <div onClick={() => setOpenGo(false)} 
          className={styles.finish}>Finish</div>
        </div>
        <div className={styles.progress}>
          <div className={styles.progress__line} style={{width: `${progress}%`}} />
        </div>
      </div>
      <div className={styles.infoExercise}>
        <div>
          <h4 className={styles.titleExercise}>{titleExercise}</h4>
          <div className={styles.countApproach}>
            Approach {countApp}/{workout.listExercises[0].listApproaches.length}
          </div>  
        </div>
      </div>
      <div className={styles.timerContainer}>
        <div className={styles.data}>
          <div className={styles.time}>
            {seconds}
          </div>
          <div id="time" className={styles.info}>Time</div>
          <div className='icon-pause' />
        </div>
      </div>
      <div className={styles.navButtons}>
        <div className={styles.btnSkip}>
          <div className={`icon-skip ${styles.icon}`} />
          {
            event === 'approach' ?
            <div onClick={() => toggleSkip()}
            className={styles.text}>Skip</div> : event === 'pause' ?
            <div onClick={() => togglePause()}
            className={styles.text}>Skip</div>
            : null
          }
        </div>
        <div className={styles.btnComplete}>
          <div className={`icon-complete ${styles.icon}`} />
          {
            event === 'approach' ?
            <div onClick={() => toggleComplete()}
            className={styles.text}>Complete</div> : event === 'pause' ?
            <div onClick={() => togglePause()}
            className={styles.text}>Complete</div>
            : null
          }
        </div>
      </div>
      <div className={styles.widgets}>
        <div className={styles.widget}>
          <div className={styles.parametr}>{weight}</div>
          <div className={styles.text}>Weight</div>
        </div>
        <div className={styles.widget}>
          {
            mainParameter === 'time' ?
            <>
            <div className={styles.parametr}>{time}</div>
            <div className={styles.text}>Time</div>
            </> : mainParameter === 'repeats' ?
            <>
            <div className={styles.parametr}>{repeats}</div>
            <div className={styles.text}>Repeats</div>
            </>
            : null
          }
        </div>
      </div>
      <div className={styles.footer}>
        <div className={styles.parameter}>
          <div className={styles.text}>
            <div className="icon-default" />
            <div className={styles.content}>Pause</div>
          </div>
          <div className={styles.info}>{pause} sec</div>
        </div>
        <div className={styles.parameter}>
          <div className={styles.text}>
            <div className="icon-skip" />
            <div className={styles.content}>Next exercise</div>
          </div>
          <div className={styles.info}>{nextExercise}</div>
        </div>
        <div className={styles.audio}>
          <audio src='/public/music/Saliki feat. 104 - Smile.mp3' controls />
        </div>
      </div>
    </div>
  )
}