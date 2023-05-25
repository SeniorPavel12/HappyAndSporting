import React from 'react'

import styles from './NavLibrary.module.scss'


export const NavLibrary = ({ setOpenSongs, setOpenPlaylists }) => {
  
  
  return (
    <div className={styles.container}>
      <h2 className={styles.titlePage}>Library</h2>
      <div className={styles.navLinks}>
        <div onClick={() => setOpenSongs(true)}
        className={styles.navSongs}>Songs</div>
        <div onClick={() => setOpenPlaylists(true)}
        className={styles.navPlaylists}>Playlists</div>
      </div>
    </div>
  )
}