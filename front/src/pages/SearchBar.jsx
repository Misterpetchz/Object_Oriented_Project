import React, { useEffect, useState } from 'react';

const SearchBar = ({searching}) => {
    const [term, setTerm] = useState('');


    useEffect(() => {
        if(term !== ''){
            searching(term);
        }
    }, [term, searching]);

    return (
      <div className='searchbar'>
        <input
            className='searchbar-input'
            type='text'
            placeholder="Input Searching..."
            onChange={e => setTerm(e.target.value)}
            value={term}/>
      </div>
    );
};

export default SearchBar;
