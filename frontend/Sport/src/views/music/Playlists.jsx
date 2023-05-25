import React, { useState } from 'react'

import styles from './Playlists.module.scss'
import { deleteEl } from '../../services/js/deleteEl'
import { useGlobalContext } from '../../services/contexts/GlobalContext'
import { PlaylistService } from '../../services/axios/playlist.service'


export const Playlists = ({ 
  setOpenPlaylists, listPlaylists, setListPlaylists, listMusic
}) => {

  const {setListGlobalPlaylists} = useGlobalContext()
  
  const [playlist, setPlaylist] = useState({
    id: undefined, title: '', listMusic: []
  })

  const createPlaylist = (e) => {
    e.preventDefault()
    const newPlaylist = {
      id: playlist.id,
      title: playlist.title,
      listMusic: playlist.listMusic
    }

    setListPlaylists(prev => [...prev, newPlaylist])
    setPlaylist({title: '', listMusic: []})
    setListGlobalPlaylists(prev => [...prev, newPlaylist])
  
    // const create = async () => {
    //   const data = await PlaylistService.create({
    //     title: newPlaylist.title
    //   })
    //   setPlaylist(prev => ({...prev, id: data}))
    // }

    // create()
  }

  const deletePlaylist = async (playlist) => {
    const data = await PlaylistService.delete({
      id: [playlist.id]
    })
  }

  const deleteMusic = async (song) => {
    const data = await MusicService.delete({
      id: [song.id]
    })
  }
  
  return (
    <div className={styles.container}>
      <div onClick={() => setOpenPlaylists(false)}
      className={`icon-prev ${styles.prev}`} />
      <div className={styles.body}>
        <div className={styles.head}>
          <form className={styles.form}>
            <input type="text" placeholder='Enter title' className={styles.input}
            onChange={e => setPlaylist(prev => ({...prev, title: e.target.value}))} value={playlist.title}
            />
            <button onClick={e => createPlaylist(e)}
            type='reset' className={styles.btn}>Add</button>
          </form>
        </div>
        <div className={styles.listPlaylist}>
          {
            listPlaylists.map((playlist, index) => (
            <div key={index} className={styles.playlist}>
              <a class={`btn btn-primary ${styles.titlePlay}`} data-bs-toggle="collapse" href={`#collapseExample${index}`} role="button" aria-expanded="false" aria-controls="collapseExample">
                {playlist.title}
                <div onClick={() => {
                  deleteEl(listPlaylists, playlist)
                  deletePlaylist(playlist)
                }}
                className='icon-delete' />
              </a>
              <div class={`collapse ${styles.card}`} id={`collapseExample${index}`}>
                <div class={`card card-body ${styles.songs}`}>
                  {
                    playlist.listMusic.map((music, index) => (
                      <div key={index} className={styles.song}>
                        <div className={styles.info}>
                          <div className={styles.title}>{music.title}</div>
                          <div className={styles.autor}>{music.autor}</div>
                        </div>
                        <div onClick={() => {
                          deleteEl(playlist.listMusic, music)
                          deleteEl(listMusic, music)
                          deleteMusic(music)
                        }}
                        className={`icon-delete ${styles.delete}`} />
                      </div>
                    ))
                  }
                </div>
              </div>   
            </div>
            ))
          }
        </div>
      </div>
    </div>
  )
}