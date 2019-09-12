import React, { useContext } from "react"
import { gql } from 'apollo-boost'
import { useLazyQuery } from '@apollo/react-hooks'

import Row from './Row'
import { RowContext } from './RowContext'

import '../css/Button.css'

const getBlocksDataQuery = gql`
{
  allBlocks {
      edges {
          node {
            blockContent
            blockId
            blockUrl
            blockType
            blockTitle
            blockCreateDate
            channelTitle
            requestId
          }
      }
  }
}
`

function RowList() {

    const [ getBlocks, {loading, data} ] = useLazyQuery(getBlocksDataQuery);
    const { rows, addRow } = useContext(RowContext);

    if (data && !loading) {
        var i;
        var j = 1;
        for (i = data.allBlocks.edges.length-3; i < data.allBlocks.edges.length; i++) {
            addRow(
                j,
                data.allBlocks.edges[i].node.blockType,
                data.allBlocks.edges[i].node.blockUrl,
                data.allBlocks.edges[i].node.blockContent,
                data.allBlocks.edges[i].node.blockTitle,
                data.allBlocks.edges[i].node.channelTitle,
                data.allBlocks.edges[i].node.blockCreateDate,
            );
            j++;
          }
    }

    if (loading) {
        return (
          <>
              {rows.map(row => {
                return (
                    <Row type={row.type} />
                )}
              )}
              <div id='button-div'>
                <button id='button' onClick={() => {
                  getBlocks();
                }}>Refresh</button>
              </div>
          </>
        )
    }

    else if (!loading) {

        console.log(rows[1]);

        return (
          <>
            {rows.map(row => {
              return (
                  <Row
                    type={row.type}
                    link={row.link}
                    content={row.content}
                    title={row.title}
                    channel={row.channel}
                    date={row.date}
                  />
              )}
            )}

            <div id='button-div'>
              <button id='button' onClick={() => {
                  getBlocks();
              }}>Refresh</button>
            </div>
          </>
        )
    }
}

//         return rows.map(row => {
//             if (row.type === 'Media' || row.type === 'Image' || row.type === 'Link' || row.type === 'Attachment') {
//               return <Row
//                   type='Media'
//                   link={row.link}
//                   content={row.content}
//                   title={row.title}
//                   channel={row.channel}
//                   date={row.date}
//               />
//             } else if (row.type === 'Text') {
//               return <Row
//                   type={row.type}
//                   link={row.link}
//                   content={row.content}
//                   title={row.title}
//                   channel={row.channel}
//                   date={row.date}
//               />
//             } else {
//               return <Row
//                   type='Empty'
//               />
//             }
//         });
//     } else {
//         return null;
//     }

export default RowList
