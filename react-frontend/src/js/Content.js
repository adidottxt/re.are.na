import React, { useContext, useEffect } from "react"
import { gql } from 'apollo-boost'
import { useQuery } from '@apollo/react-hooks'

import Row from './Row'
import { ContentContext } from './ContentContext'

import '../css/Content.css'

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

var requestSent = false;
var setLoading = true;

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

      if ((networkStatus === 4) && setLoading) {
        var new_data = [
          {type: 'Empty', link: '', content: '', title: '', channel: '', date: ''},
          {type: 'Empty', link: '', content: '', title: '', channel: '', date: ''},
          {type: 'Empty', link: '', content: '', title: '', channel: '', date: ''},
        ];
        addEmptyRows(new_data);
        setLoading = false;
        refetch();
      }

      if (!loading && requestSent) {
        new_data = data.allBlocks.edges.slice(data.allBlocks.edges.length - 3);
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
