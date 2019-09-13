import React, { createContext, useState } from 'react';

export const RowContext = createContext();

const RowContextProvider = (props) => {
    const [rows, setRows] = useState([
      {type: 'Empty', link: '', content: '', title: '', channel: '', date: ''},
      {type: 'Empty', link: '', content: '', title: '', channel: '', date: ''},
      {type: 'Empty', link: '', content: '', title: '', channel: '', date: ''},
    ])

    const addRows = (new_rows) => {
      console.log('before', rows);
      setRows(new_rows.map(row => {
          return (
              {
                type: row.node.blockType,
                link: row.node.blockUrl,
                content: row.node.blockContent,
                channel: row.node.channelTitle,
                date: row.node.blockCreateDate,
                title: row.node.blockTitle,
              }
          )
      }))
      console.log('after', rows);
    }

    return (
      <RowContext.Provider value={{rows, addRows}}>
        {props.children}
      </RowContext.Provider>
    )
}

export default RowContextProvider
