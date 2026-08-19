import { useState } from "react";

import movies from "./data/movie_list.json";


function App() {

  const [selectedId, setSelectedId] = useState(
    movies[0]?.movie_id ?? ""
  );


  const selectedMovie = movies.find(
    (movie) =>
      movie.movie_id === Number(selectedId)
  );


  return (
    <main className="page">

      <section className="container">

        {/* Page Header */}
        <header>

          <p className="eyebrow">
            Best Movie Scope
          </p>

          <h1>
            Movie Explorer
          </h1>

          <p className="subtitle">
            Select a movie to see its ratings
            and genres.
          </p>

        </header>


        {/* Movie Dropdown */}
        <section className="selector-card">

          <label htmlFor="movie-select">
            Movie title
          </label>


          <select
            id="movie-select"
            value={selectedId}
            onChange={(event) =>
              setSelectedId(event.target.value)
            }
          >

            {movies.map((movie) => (

              <option
                key={movie.movie_id}
                value={movie.movie_id}
              >
                {movie.movie_title}
              </option>

            ))}

          </select>

        </section>


        {/* Movie Information */}
        {selectedMovie && (

          <section className="movie-card">

            <h2>
              {selectedMovie.movie_title}
            </h2>


            <div className="stats">

              {/* Number of ratings */}
              <div className="stat">

                <span className="label">
                  Number of ratings
                </span>

                <strong>
                  {selectedMovie.cnt_rating}
                </strong>

              </div>


              {/* Average score */}
              <div className="stat">

                <span className="label">
                  Average score
                </span>

                <strong>
                  {Number(
                    selectedMovie.avg_rating
                  ).toFixed(2)}
                </strong>

              </div>


              {/* Genres */}
              <div className="stat genres">

                <span className="label">
                  Genres
                </span>

                <div className="genre-list">

                  {selectedMovie.genres.map(
                    (genre) => (

                      <span
                        className="genre"
                        key={genre}
                      >
                        {genre}
                      </span>

                    )
                  )}

                </div>

              </div>

            </div>

          </section>

        )}

      </section>

    </main>
  );
}


export default App;