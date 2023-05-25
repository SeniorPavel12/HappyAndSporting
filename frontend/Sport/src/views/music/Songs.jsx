import React from 'react'

import styles from './Songs.module.scss'
import { deleteEl } from '../../services/js/deleteEl'
import { MusicService } from '../../services/axios/music.service'


export const Songs = ({ 
  setOpenSongs, listMusic, listPlaylists 
}) => {
  
  const deleteData = async (song) => {
    const data = await MusicService.delete({
      id: [song.id]
    })
  }

  const editData = async (song) => {
    const data = await MusicService.edit({
      title: song.title,
      playlist: song.playlist
    })
  }
  
  return (
    <div className={styles.container}>
      <div onClick={() => setOpenSongs(false)}
      className={`icon-prev ${styles.prev}`} />
      <div className={styles.listSongs}>
        {
          listMusic.map((music, index) => (
          <div key={index} className={styles.song}>
            <div className={styles.info}>
              <div className={styles.title}>{music.title}</div>
              <div className={styles.autor}>{music.autor}</div>
            </div>
            <div className={styles.playlists}>
              <select defaultValue={`${music.playlist}`} onChange={(e) => {
                music.playlist = e.target.value
                for (let playlist of listPlaylists) {
                  if (playlist.listMusic.includes(music)) {
                    deleteEl(playlist.listMusic, music)
                  } else if (playlist.title === music.playlist) {
                    playlist.listMusic.push(music)
                  }
                }
                editData(music)
              }} name="playlists" id="addToPlaylists">
                <option value={'None'}>None</option>
                {
                  listPlaylists.map((playlist, index) => (
                    <option value={`${playlist.title}`} key={index}>{playlist.title}</option>
                  ))
                }
              </select>
              <div onClick={() => {
                deleteEl(listMusic, music)
                deleteData(music)
                for (let playlist of listPlaylists) {
                  if (playlist.listMusic.includes(music)) {
                    deleteEl(playlist.listMusic, music)
                  }
                }
              }} className='icon-delete' />
            </div>
          </div>
          ))
        }
      </div>
    </div>
  )
}