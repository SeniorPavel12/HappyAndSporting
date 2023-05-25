import React, { useState } from "react"

import styles from "./Approach.module.scss"


export const Approach = ({ approach, countApp, typeExercise }) => {


  const [mainParametr, setMainParametr] = useState(approach.mainParametr)
  const [weight, setWeight] = useState(approach.weight)

  const increment = (parameter) => {
    if (parameter === 'mainParametr') {
      setMainParametr(prev => prev + 5)
      approach.mainParametr = mainParametr + 5
    } else if (parameter === 'weight') {
      setWeight(prev => prev + 5)
      approach.weight = weight + 5
    }
  }

  const decrement = (parameter) => {
    if (parameter === 'mainParametr' && mainParametr > 0) {
      setMainParametr(prev => prev - 5)
      approach.mainParametr = mainParametr - 5
    } else if (parameter === 'weight' && weight > 0) {
      setWeight(prev => prev - 5)
      approach.weight = weight - 5
    }
  }

  return (
    <div className={styles.approach}>
      <div className={styles.headApproach}>
        <h3>Approach {countApp}</h3>
      </div>
      <div className={styles.bodyApproach}>
        <div className={styles.parameter}>
          <div className={styles.title}>
            <div className="icon-1" />
            <div className={styles.text}>
              {
                typeExercise === 'repeat' ? 'Repeats' : 'Time'
              }
            </div>
          </div>
          <div className={styles.tuning}>
            <div onClick={() => decrement("mainParametr")} className={styles.minus}>-</div>
            <div className={styles.count}>{mainParametr}</div>
            <div onClick={() => increment("mainParametr")} className={styles.plus}>+</div>
          </div>
        </div>
        <div className={styles.parameter}>
          <div className={styles.title}>
            <div className="icon-2" />
            <div className={styles.text}>Weight</div>
          </div>
          <div className={styles.tuning}>
            <div onClick={() => decrement("weight")} className={styles.minus}>-</div>
            <div className={styles.count}>{weight}</div>
            <div onClick={() => increment("weight")} className={styles.plus}>+</div>
          </div>
        </div>
      </div>
    </div>    
  )
}