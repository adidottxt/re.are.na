import React, { useContext } from "react"
import { gql } from 'apollo-boost'
import { useQuery } from '@apollo/react-hooks'

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
    console.log('re-rendering')
    const { loading, error, data } = useQuery(getBlocksDataQuery);
    const { rows, addRow } = useContext(RowContext);

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
                  console.log('first state');
                  console.log('rows pre add');
                  console.log(rows);
                  // for (i = 1; i < data.allBlocks.edges.length; i++) {
                  //     addRow(
                  //         i,
                  //         data.allBlocks.edges[i].node.blockType,
                  //         data.allBlocks.edges[i].node.blockUrl,
                  //         data.allBlocks.edges[i].node.blockContent,
                  //         data.allBlocks.edges[i].node.blockTitle,
                  //         data.allBlocks.edges[i].node.channelTitle,
                  //         data.allBlocks.edges[i].node.blockCreateDate,
                  //     )
                  // }
              }}>Refresh</button>
            </div>
          </>
        )
    }

    else {
        console.log('done loading');

        if (error) return "Error! $(error.message)";

        var i = 0;
        var highestRequest = 0;
        var requestId = 0;

        for (i = 0; i < data.allBlocks.edges.length; i++) {
            requestId = Number(data.allBlocks.edges[i].node.requestId)
            if (requestId > highestRequest) {
                highestRequest = requestId;
            }
        }

        console.log('post loading, these are the rows');
        console.log(rows);

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
                  console.log('second state');
                  console.log(rows);
                  for (i = 1; i < data.allBlocks.edges.length; i++) {
                      addRow(
                          i,
                          data.allBlocks.edges[i].node.blockType,
                          data.allBlocks.edges[i].node.blockUrl,
                          data.allBlocks.edges[i].node.blockContent,
                          data.allBlocks.edges[i].node.blockTitle,
                          data.allBlocks.edges[i].node.channelTitle,
                          data.allBlocks.edges[i].node.blockCreateDate,
                      )
                  }
              }}>Refresh</button>
            </div>
          </>
        )
    }
}

export default RowList
