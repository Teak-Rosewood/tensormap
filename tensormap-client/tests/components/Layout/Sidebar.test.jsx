import { render, fireEvent } from "@testing-library/react";
import Sidebar from "../../../src/components/DragAndDropCanvas/Sidebar";
import "@testing-library/jest-dom";

describe("<Sidebar />", () => {
  it("renders without crashing", () => {
    const { getByText } = render(<Sidebar />);
    expect(getByText("Input Node")).toBeInTheDocument();
    expect(getByText("Dense Node")).toBeInTheDocument();
    expect(getByText("Flatten Node")).toBeInTheDocument();
  });

  it("sets correct dataTransfer values when nodes are dragged", () => {
    const { getByText } = render(<Sidebar />);
    const dataTransferMock = {
      setData: jest.fn(),
      effectAllowed: "",
    };

    fireEvent.dragStart(getByText("Input Node"), {
      dataTransfer: dataTransferMock,
    });
    expect(dataTransferMock.setData).toHaveBeenCalledWith(
      "application/reactflow",
      "custominput",
    );
    expect(dataTransferMock.effectAllowed).toBe("move");

    fireEvent.dragStart(getByText("Dense Node"), {
      dataTransfer: dataTransferMock,
    });
    expect(dataTransferMock.setData).toHaveBeenCalledWith(
      "application/reactflow",
      "customdense",
    );

    fireEvent.dragStart(getByText("Flatten Node"), {
      dataTransfer: dataTransferMock,
    });
    expect(dataTransferMock.setData).toHaveBeenCalledWith(
      "application/reactflow",
      "customflatten",
    );
  });
});
