import React, { useState } from 'react'

import styles from './Add.module.scss'
import { MusicService } from '../../services/axios/music.service'


export const Add = ({ setListMusic, listPlaylists, setListPlaylists }) => {
  
  const [title, setTitle] = useState('')
  const [autor, setAutor] = useState('')
  const [playlist, setPlaylist] = useState('None')
  const [file, setFile] = useState('')
  const [id, setId] = useState(undefined)

  const createSongs = () => {
    const newSong = {
      id: id,
      title: title,
      autor: autor,
      playlist: playlist,
      file: file
    }

    const clean = () => {
      setTitle('')
      setAutor('')
      setPlaylist('')
      setFile(undefined)
    }

    const validation = () => {
      if (newSong.title === '') {
        alert('Enter the title')
      } else if (newSong.autor === '') {
        alert('Enter the autor')
      } else if (newSong.file === '') {
        alert('Add the MP3 file')
      } else {
        setListMusic(prev => [...prev, newSong])
        for (let playlist of listPlaylists) {
          if (playlist.title === newSong.playlist) {
            playlist.listMusic.push(newSong)
          }
        }
        setListPlaylists(listPlaylists)
        clean()
        console.log(newSong);
      }
    }

    validation()

    // const create = async () => {
    //   const data = await MusicService.create({
    //     title: newSong.title,
    //     content: newSong.file,
    //   })
    //   setId(data)
    // }

    // const addToPlaylist = async () => {
    //   const data = await MusicService.create({
    //     music: [newSong.id]
    //   })
    // }

    // const edit = async () => {
    //   const data = await MusicService.edit({
    //     title: song.title,
    //     playlist: newSong.playlist
    //   })
    // }

    // create()
    // addToPlaylist()
    // edit()
  }
  
  return (
    <div className={styles.form}>
      <form action="#" id="form" className="formBody">
        <div className={styles.formItem}>
          <label htmlFor="formTitle" className={styles.formLabel}>Title:</label>
          <input type="text" id="formTitle" name="title" className={styles.formInput}
          onChange={e => setTitle(e.target.value)} value={title}
          />
        </div>
        <div className={styles.formItem}>
          <label htmlFor="formName" className={styles.formLabel}>Autor:</label>
          <input type="text" id="formName" name="name" className={styles.formInput}
          onChange={e => setAutor(e.target.value)} value={autor}
          />
        </div>
        <div className={styles.formItem}>
          <label htmlFor="formPlaylist" className={styles.formLabel}>Playlist:</label>
          <select onChange={e => setPlaylist(e.target.value)} value={playlist}>
            <option>None</option>
            {
              listPlaylists.map((playlist, index) => (
                <option key={index}>{playlist.title}</option>
              ))
            }
          </select>
        </div>
        <div className={styles.formItem}>
          <div className={styles.formLabel}>MP3 file</div>
          <div className={styles.file}>
            <div className={styles.fileItem}>
              <input accept=".mp3" type="file" id="formFile" name="file" className={styles.fileInput}
              onChange={e => setFile(e.target.value)} value={file}
              />
              <div className={styles.fileButton}>Choose</div>
            </div>
            <div id="formPreview" className={styles.filePreview}></div>
          </div>
        </div>
        <button onClick={createSongs} type="reset" className={styles.formButton}>Add</button>
      </form>
    </div>
  )
}