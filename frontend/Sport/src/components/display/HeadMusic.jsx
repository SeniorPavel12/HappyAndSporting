import React from 'react'

import styles from './HeadMusic.module.scss'


export const HeadMusic = ({ setOpenAdd, setOpenLibrary }) => {
  
  
  return (
    <div className={styles.header}>
      <div className={styles.titlePage}>
        Music
      </div>
      <div className={styles.navLinks}>
        <div onClick={() => {
          setOpenAdd(true)
          setOpenLibrary(false)
        }}
        className={styles.nav}>Add</div>
        <div onClick={() => {
          setOpenLibrary(true)
          setOpenAdd(false)
        }}
        className={styles.nav}>Library</div>
      </div>
    </div>
  )
}