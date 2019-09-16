import React, { useContext, useEffect } from "react"
import { gql } from 'apollo-boost'
import { useQuery } from '@apollo/react-hooks'

import Row from '../rows/Row'
import { ContentContext } from './ContentContext'

import '../../css/Content.css'


var requestSent = false;
var setLoading = true;
const refetchValue = 4;
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
      }
    }
  }
}
`

function Content() {

  const { loading, data, refetch, networkStatus } = useQuery(getBlocksDataQuery, {
    notifyOnNetworkStatusChange: true,
  });
  const { rows, addRows, addEmptyRows } = useContext(ContentContext);

  function refetchAndReload() {
    setLoading = true;
    requestSent = true;
    refetch();
  }

  useEffect(() => {
    if (loading) {
      requestSent = true;
    }

    if ((networkStatus === refetchValue) && setLoading) {
      addEmptyRows();
      setLoading = false;
      refetch();
    }

    if (!loading && requestSent) {
      var new_data = data.allBlocks.edges.slice(data.allBlocks.edges.length - 3);
      addRows(new_data);
      requestSent = false;
    }
  });

  return (
    <>
      {rows.map((row, index) => {
        return (
          <Row
            key={index}
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
          refetchAndReload();
        }}>Refresh</button>
      </div>
    </>
  )
}

export default Content
