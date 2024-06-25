import { useState, useEffect } from "react"
import { useParams } from "react-router-dom"
import io from "socket.io-client"

const socket = io.connect('http://localhost:3001') 

const GamePage = (props) => {
  let params = useParams()['*']

  const [gameData, setGameData] = useState([
    ['','',''],
    ['','',''],
    ['','','']
  ])
  const player = 'x'

  useEffect(() => {
    socket.on('reciveGameData', (data) => {
      setGameData(data)
    })
  }, [socket])


  const sendGameData = () => {
    socket.emit('gameStateChanged', gameData)
  }
  const joinRoom = () => {
    socket.emit('joinGame', props.gameId)
  }

  return (
    <div>
      <button onClick={sendGameData}>click me</button>
      <div className='game-container'>
          <div>Loading...</div>
          <div className='tic-tac-toe-grid'>
            {gameData.map((row, index1) => 
            <>
              {row.map((val, index2) => 
                <button onClick={() => {
                  let tempGameData = gameData
                  tempGameData[index1][index2] = player 
                }}>
                  {val}
                </button>
              )}
            </>
            )}
        </div>
      </div>
    </div>
  )
}



export default GamePage