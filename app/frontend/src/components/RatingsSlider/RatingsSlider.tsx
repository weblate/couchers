import Slider from "@material-ui/core/Slider";
import {
  AMAZING,
  NEGATIVE,
  NEUTRAL,
  POSITIVE,
  RATINGS_SLIDER,
} from "components/RatingsSlider/constants";
import { handleSliderChange } from "components/RatingsSlider/functions";
import SliderLabel from "components/RatingsSlider/SliderLabel";
import React, { useRef } from "react";
import makeStyles from "utils/makeStyles";

const useStyles = makeStyles((theme) => ({
  root: {
    '& .MuiSlider-markLabel[data-index="0"]': {
      transform: "translateX(0%)",
    },
    height: "0.5rem",
    borderRadius: "1.5625rem",
    marginTop: theme.spacing(6),
    marginBottom: theme.spacing(1),
  },
  track: {
    height: "0.625rem",
    borderRadius: "1.5625rem",
  },
  rail: {
    height: "0.625rem",
    borderRadius: "1.5625rem",
  },
  thumb: {
    height: "1.25rem",
    width: "1.25rem",
    color: theme.palette.badRating.main,
  },
  valueLabel: {
    left: "calc(-50% + 0.25rem)",
  },
  mark: {
    display: "none",
  },
}));

const marks = [
  {
    value: 0,
    label: `${NEGATIVE}`,
  },
  {
    value: 0.25,
    label: `${NEUTRAL}`,
  },
  {
    value: 0.5,
    label: `${POSITIVE}`,
  },
  {
    value: 0.85,
    label: `${AMAZING}`,
  },
];

interface SliderProps {
  defaultValue: number;
  onChange?: (value: number | number[]) => void;
}

export default function RatingsSlider({ defaultValue, onChange }: SliderProps) {
  const sliderRef = useRef<HTMLSpanElement>(null);
  const classes = useStyles();

  return (
    <Slider
      ref={sliderRef}
      classes={{
        root: classes.root,
        thumb: classes.thumb,
        track: classes.track,
        rail: classes.rail,
        valueLabel: classes.valueLabel,
        mark: classes.mark,
      }}
      aria-label={RATINGS_SLIDER}
      defaultValue={defaultValue}
      min={0}
      max={1}
      step={0.01}
      marks={marks}
      valueLabelDisplay="on"
      valueLabelFormat={(value) => <SliderLabel value={value} />}
      onChange={(event, value) => {
        handleSliderChange(sliderRef, value);
        onChange?.(value);
      }}
    />
  );
}
