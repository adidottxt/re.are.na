import React, { createContext, useState } from 'react';

export const RowContext = createContext();

const RowContextProvider = (props) => {
    const [rows, setRows] = useState([
      {type: 'Empty', link: '', content: '', title: '', channel: '', date: '', id:1},
      {type: 'Empty', link: '', content: '', title: '', channel: '', date: '', id:2},
      {type: 'Empty', link: '', content: '', title: '', channel: '', date: '', id:3},
    ])

    const addRow = (id, type, link, content, title, channel, date) => {
        setRows(rows[id-1] = {type: type, link: link, content: content, title: title, channel: channel, date: date, id: id});
    }

    return (
      <RowContext.Provider value={{rows, addRow}}>
        {props.children}
      </RowContext.Provider>
    )
}

export default RowContextProvider
