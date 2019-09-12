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
        console.log('added row', type, date);
        console.log(rows.length, id);
        console.log(rows);
    }

    const removeRows = (id, type) => {
        setRows(rows[id] = {});
        console.log('removed all rows!');
        console.log(rows.length);
        console.log(rows);
    }

    const addEmptyRows = (id) => {
        setRows(rows[id-1] = {type: 'Empty', link: '', content: '', title: '', channel: '', date: '', id:id});
        console.log('added empty rows');
        console.log(rows.length);
        console.log(rows);
    }

    return (
      <RowContext.Provider value={{rows, addRow, removeRows, addEmptyRows}}>
        {props.children}
      </RowContext.Provider>
    )
}

export default RowContextProvider
